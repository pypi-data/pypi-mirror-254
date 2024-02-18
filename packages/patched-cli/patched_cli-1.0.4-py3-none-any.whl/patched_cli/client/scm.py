import functools
from dataclasses import dataclass
from typing import Protocol

import gitlab.const
import sentry_sdk
from github import Auth, Consts, Github
from github.PullRequest import PullRequest
from gitlab import Gitlab
from gitlab.v4.objects import ProjectMergeRequest


@dataclass(slots=True)
class Comment:
    path: str
    body: str
    start_line: int | None
    end_line: int


class PullRequestProtocol(Protocol):
    def url(self) -> str:
        ...

    def set_body(self, body: str) -> None:
        ...

    def create_comment(self, comment: Comment) -> str | None:
        ...

    def reset_comments(self) -> None:
        ...


class ScmPlatformClientProtocol(Protocol):
    def test(self) -> bool:
        ...

    def set_url(self, url: str) -> None:
        ...

    def find_pr(self, slug, original_branch: str, feature_branch: str) -> PullRequestProtocol | None:
        ...

    def create_pr(
        self,
        slug: str,
        title: str,
        body: str,
        original_branch: str,
        feature_branch: str,
    ) -> PullRequestProtocol:
        ...


class GitlabMergeRequest:
    def __init__(self, mr: ProjectMergeRequest):
        self._mr = mr

    def url(self) -> str:
        return self._mr.web_url

    def set_body(self, body: str) -> None:
        self._mr.description = body
        self._mr.save()

    def create_comment(self, comment: Comment) -> str | None:
        while True:
            try:
                commit = self._mr.commits().next()
            except StopIteration:
                continue

            break

        while True:
            try:
                iterator = self._mr.diffs.list(iterator=True)
                diff = iterator.next()  # type: ignore
            except StopIteration:
                continue

            if diff.head_commit_sha == commit.get_id():
                break

        base_commit = diff.base_commit_sha
        head_commit = diff.head_commit_sha

        try:
            discussion = self._mr.discussions.create(
                {
                    "body": comment.body,
                    "position": {
                        "base_sha": base_commit,
                        "start_sha": base_commit,
                        "head_sha": head_commit,
                        "position_type": "text",
                        "old_path": comment.path,
                        "new_path": comment.path,
                        "old_line": comment.end_line,
                        "new_line": comment.end_line,
                    },
                }
            )
        except Exception as e:
            sentry_sdk.capture_exception(e)
            return None

        for note in discussion.attributes["notes"]:
            return f"#note_{note['id']}"

        return None

    def reset_comments(self) -> None:
        for discussion in self._mr.discussions.list():
            for note in discussion.attributes["notes"]:
                if note["type"] == "DiffNote":
                    discussion.notes.delete(note["id"])


class GithubPullRequest:
    def __init__(self, pr: PullRequest):
        self._pr = pr

    def url(self) -> str:
        return self._pr.html_url

    def set_body(self, body: str) -> None:
        self._pr.edit(body=body)

    def create_comment(self, comment: Comment) -> str:
        kwargs = {
            "path": comment.path,
            "body": comment.body,
            "line": comment.end_line,
            "side": "LEFT",
        }
        if comment.start_line is not None:
            kwargs["start_line"] = comment.start_line
            kwargs["start_side"] = "LEFT"

        return self._pr.create_review_comment(commit=self._pr.get_commits()[0], **kwargs).html_url  # type: ignore

    def reset_comments(self) -> None:
        for comment in self._pr.get_review_comments():
            comment.delete()


class GithubClient:
    DEFAULT_URL = Consts.DEFAULT_BASE_URL

    def __init__(self, access_token: str, url: str = DEFAULT_URL):
        self._access_token = access_token
        self._url = url

    @functools.cached_property
    def github(self) -> Github:
        auth = Auth.Token(self._access_token)
        return Github(base_url=self._url, auth=auth)

    def test(self) -> bool:
        return True

    def set_url(self, url: str) -> None:
        self._url = url

    def find_pr(self, slug, original_branch: str, feature_branch: str) -> PullRequestProtocol | None:
        repo = self.github.get_repo(slug)
        pages = repo.get_pulls(base=original_branch, head=feature_branch)
        for pr in iter(pages):
            if pr.base.ref == original_branch and pr.head.ref == feature_branch:
                return GithubPullRequest(pr)

        return None

    def create_pr(
        self,
        slug: str,
        title: str,
        body: str,
        original_branch: str,
        feature_branch: str,
    ) -> PullRequestProtocol:
        repo = self.github.get_repo(slug)
        pr = self.find_pr(slug, original_branch, feature_branch)
        if pr is None:
            gh_pr = repo.create_pull(title=title, body=body, base=original_branch, head=feature_branch)
            pr = GithubPullRequest(gh_pr)

        return pr


class GitlabClient:
    DEFAULT_URL = gitlab.const.DEFAULT_URL

    def __init__(self, access_token: str, url: str = DEFAULT_URL):
        self._access_token = access_token
        self._url = url

    @functools.cached_property
    def gitlab(self) -> Gitlab:
        return Gitlab(self._url, private_token=self._access_token)

    def set_url(self, url: str) -> None:
        self._url = url

    def test(self) -> bool:
        self.gitlab.auth()
        return self.gitlab.user is not None

    def find_pr(self, slug, original_branch: str, feature_branch: str) -> PullRequestProtocol | None:
        project = self.gitlab.projects.get(slug)
        mrs = project.mergerequests.list(
            iterator=True,
            **{
                "state": "opened",
                "source_branch": feature_branch,
                "target_branch": original_branch,
            },
        )

        mr: ProjectMergeRequest
        try:
            mr = mrs.next()  # type: ignore
        except StopIteration:
            return None

        return GitlabMergeRequest(mr)

    def create_pr(
        self,
        slug: str,
        title: str,
        body: str,
        original_branch: str,
        feature_branch: str,
    ) -> PullRequestProtocol:
        mr = self.find_pr(slug, original_branch, feature_branch)
        if mr is None:
            project = self.gitlab.projects.get(slug)
            gl_mr = project.mergerequests.create(
                {
                    "source_branch": feature_branch,
                    "target_branch": original_branch,
                    "title": title,
                    "description": body,
                }
            )
            mr = GitlabMergeRequest(gl_mr)  # type: ignore

        return mr
