import contextlib
from typing import Dict, Generator, List

import click
from git import Repo, Head
from unidiff import PatchSet
from unidiff.patch import Line

from patched_cli.client.patched import PatchedClient
from patched_cli.client.scm import Comment, ScmPlatformClientProtocol
from patched_cli.models.common import Patch, PatchMessage
from patched_cli.models.records import PrCreationResult, LocalRepository
from patched_cli.utils.noop import noop
from patched_cli.utils.logging import logger

def get_slug_from_remote_url(remote_url: str) -> str:
    # TODO: consider using https://github.com/nephila/giturlparse instead
    if remote_url.startswith("git@"):
        # ssh
        _, _, potential_slug = remote_url.partition(":")
    else:
        potential_slug = "/".join(remote_url.split("/")[-2:])

    return potential_slug.removesuffix(".git")


@contextlib.contextmanager
def transitioning_branches(repo: Repo, is_new_branch: bool) -> Generator[tuple[Head, Head], None, None]:
    current_branch = repo.active_branch
    # default noop
    final_func = noop
    next_branch = current_branch
    if is_new_branch:
        next_branch_name = f"patched-{current_branch.name}"
        logger.info(f'Creating new branch "{next_branch_name}".')
        final_func = current_branch.checkout
        next_branch = repo.create_head(next_branch_name, force=True)

    try:
        next_branch.checkout()
        yield current_branch, next_branch
    finally:
        final_func()


class _EphemeralGitConfig:
    _DEFAULT = -2378137912

    def __init__(self, repo: Repo):
        self._repo = repo
        self._keys: set[tuple[str, str]] = set()
        self._original_values: Dict[tuple[str, str], str] = dict()
        self._modified_values: Dict[tuple[str, str], str] = dict()

    def set_value(self, section: str, option: str, value: str):
        self._keys.add((section, option))
        self._modified_values[(section, option)] = value

    @contextlib.contextmanager
    def context(self):
        try:
            self._persist_values_to_be_modified()
            yield
        finally:
            self._undo_modified_values()

    def _persist_values_to_be_modified(self):
        reader = self._repo.config_reader("repository")
        for section, option in self._keys:
            original_value = reader.get_value(section, option, self._DEFAULT)
            if original_value != self._DEFAULT:
                self._original_values[(section, option)] = original_value

        writer = self._repo.config_writer()
        try:
            for section, option in self._keys:
                writer.set_value(section, option, self._modified_values[(section, option)])
        finally:
            writer.release()

    def _undo_modified_values(self):
        writer = self._repo.config_writer()
        try:
            for section, option in self._keys:
                original_value = self._original_values.get((section, option), None)
                if original_value is None:
                    writer.remove_option(section, option)
                else:
                    writer.set_value(section, option, original_value)
        finally:
            writer.release()


def commit_with_msg(repo: Repo, msg: str):
    ephemeral = _EphemeralGitConfig(repo)
    ephemeral.set_value("user", "name", "patched.codes[bot]")
    ephemeral.set_value("user", "email", "298395+patched.codes[bot]@users.noreply.github.com")

    with ephemeral.context():
        repo.git.commit(
            "--author",
            "patched.codes[bot]<298395+patched.codes[bot]@users.noreply.github.com>",
            "-m",
            msg,
        )


def create_branch_and_pr(
        local_repo: LocalRepository,
        applied_patches: List[Patch],
        is_create_pr: bool,
        scm_client: ScmPlatformClientProtocol | None,
        patched_client: PatchedClient | None,
) -> PrCreationResult:
    repo: Repo = local_repo.repo  # type: ignore

    with transitioning_branches(repo, local_repo.is_new_branch) as (current_branch, next_branch):
        # git add
        for applied_patch in applied_patches:
            repo.git.add(applied_patch.path)

        commit_with_msg(repo, "Patched!")

        if not is_create_pr or (scm_client is None and patched_client is None):
            return PrCreationResult(
                message=f'Branch created at: "{next_branch.name}"',
                branch_name=next_branch.name,
                pr_url=None,
            )

        tracking_branch = current_branch.tracking_branch()
        if tracking_branch is None:
            msg = (
                "Unable to create pull request as base branch does not track a remote branch. \n"
                f'Branch created at: "{next_branch.name}"'
            )
            return PrCreationResult(message=msg, branch_name=next_branch.name, pr_url=None)

        original_remote_name = tracking_branch.remote_name
        original_remote_url = repo.remotes[original_remote_name].url

        logger.info(f'Creating pull request for branch "{next_branch.name}" to merge into "{current_branch.name}".')
        # force push, assume we have control
        repo.git.push("-f", "--set-upstream", original_remote_name, next_branch.name)

        repo_slug = get_slug_from_remote_url(original_remote_url)
        diff_text = repo.git.diff(current_branch.name)

        if scm_client is not None:
            url = create_pr(
                repo_slug,
                str(local_repo.path),
                diff_text,
                current_branch.name,
                next_branch.name,
                applied_patches,
                scm_client,
            )
        elif patched_client is not None:
            url = patched_client.create_pr(
                repo_slug,
                str(local_repo.path),
                diff_text,
                current_branch.name,
                next_branch.name,
                applied_patches,
            )
        else:
            raise ValueError("Either scm_client or patched_client must be provided")

        return PrCreationResult(
            message=f'Pull request generated at: "{url}"',
            branch_name=next_branch.name,
            pr_url=url,
        )


def create_pr(
        repo_slug: str,
        path: str,
        diff_text: str,
        original_branch_name: str,
        next_branch_name: str,
        applied_patches: List[Patch],
        scm_client: ScmPlatformClientProtocol,
):
    body = "This is an automated pull request generated by patched."
    pr = scm_client.create_pr(
        repo_slug,
        f"Patched results for branch: {original_branch_name}",
        body,
        original_branch_name,
        next_branch_name,
    )

    # reset prs by clearing previous comments
    pr.reset_comments()

    comment_md_links = []
    for patch_msg, comment in create_comments(applied_patches, diff_text, path):
        logger.debug(f"Creating comment: {comment}")
        gh_comment_url = pr.create_comment(comment)
        if gh_comment_url is None:
            continue
        comment_md_links.append(f"[{patch_msg.title}]({gh_comment_url})")

    body_items = []
    for comment_md_link in comment_md_links:
        body_items.append(f" *  {comment_md_link}")
    new_body = "\n".join([body, "------", *body_items])
    pr.set_body(new_body)

    return pr.url()


def create_comment(path, patch_message: PatchMessage, hunks: List[List[Line]]) -> Comment | None:
    if len(hunks) < 1:
        return None
    elif len(hunks) == 1 and len(hunks[0]) == 1:
        start_line = None
        end_line = hunks[0][0]
    else:
        start_line = end_line = None
        for lines in hunks:
            for line in lines:
                if line.source_line_no is None:
                    continue
                if patch_message.start_line <= line.source_line_no <= patch_message.end_line:
                    if start_line is None:
                        start_line = line
                    end_line = line

                if start_line is end_line:
                    start_line = None

    if end_line is None:
        return None

    start_line_no = None
    if start_line is not None:
        start_line_no = start_line.target_line_no if start_line.is_added else start_line.source_line_no

    end_line_no = end_line.target_line_no if end_line.is_added else end_line.source_line_no

    body = f"""
{patch_message.title}
------
{patch_message.msg}
"""
    rv = Comment(path=path, body=body, start_line=start_line_no, end_line=end_line_no)
    return rv


def create_comments(
        applied_patches: List[Patch], diff_text: str, path: str
) -> Generator[tuple[PatchMessage, Comment], None, None]:
    diffs = PatchSet(diff_text)
    diff_lines: Dict[str, Line] = {diff.path: [[line for line in hunk] for hunk in diff] for diff in diffs}
    for applied_patch in applied_patches:
        git_file_path = applied_patch.path.removeprefix(path + "/")
        hunks: List[List[Line]] = diff_lines.get(git_file_path, [])
        for patch_message in applied_patch.msgs:
            yv = create_comment(git_file_path, patch_message, hunks)
            if yv is None:
                continue

            yield patch_message, yv


def wipe_null(obj: dict):
    rv = dict()
    for key, value in obj.items():
        if value is not None:
            rv[key] = value
    return rv
