from pathlib import Path
from semgrep.ignores import FileIgnore, Parser

from patched_cli.utils.managed_files import IGNORE_NAME


class PatchedIgnore:
    def __init__(self, path: Path | None = None):
        if path is None:
            self._ignore = None
            return

        ignore_file = path / IGNORE_NAME
        if not ignore_file.exists() and not ignore_file.is_file():
            self._ignore = None
            return

        with open(ignore_file, "r") as f:
            patterns = Parser(file_path=ignore_file, base_path=path).parse(f)
        self._ignore = FileIgnore.from_unprocessed_patterns(base_path=path, patterns=patterns)

    def is_ignored(self, path: Path | str) -> bool:
        if self._ignore is None:
            return False

        if isinstance(path, str):
            path = Path(path)

        return not self._ignore._filter(path)
