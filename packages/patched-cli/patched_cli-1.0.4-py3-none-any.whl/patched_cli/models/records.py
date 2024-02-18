import pathlib
from dataclasses import dataclass, field
from typing import Protocol

from git import Repo


@dataclass(slots=True)
class PrCreationResult:
    message: str
    branch_name: str
    pr_url: str | None


@dataclass(slots=True)
class LocalRepository:
    path: pathlib.Path
    repo: Repo | None
    is_new_branch: bool
    repo_path: pathlib.Path | None = field(init=False)
    remote_url: str | None = field(init=False)
    original_branch_name: str | None = field(init=False)
    is_dirty: bool = field(init=False)
    is_non_git: bool = field(init=False)

    def __post_init__(self):
        if self.repo is None:
            self.repo_path = None
            self.is_non_git = True
            self.is_dirty = False
            self.original_branch_name = None
            self.remote_url = self.path.absolute().as_uri()
            return

        self.repo_path = pathlib.Path(self.repo.working_dir)
        self.is_dirty = self.repo.is_dirty()
        self.original_branch_name = self.repo.active_branch.name
        tracking_branch = self.repo.active_branch.tracking_branch()
        if tracking_branch is not None:
            self.remote_url = self.repo.remotes[tracking_branch.remote_name].url
        else:
            self.remote_url = None
