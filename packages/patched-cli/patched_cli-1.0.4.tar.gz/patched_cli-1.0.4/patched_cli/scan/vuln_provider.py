import json
import pathlib
import re
import subprocess
from collections import defaultdict
from typing import Any, Protocol

from patched_cli.client.sonar import SonarClient
from patched_cli.models.common import Vuln, VulnFile, Cwe
from patched_cli.scan.severity import SemgrepSeverity
from patched_cli.utils.ignore import PatchedIgnore


class VulnProviderProtocol(Protocol):
    def run_provider(self, ignore: PatchedIgnore) -> list[VulnFile]:
        ...

    def run_tool(self) -> Any:
        ...

    def read_vuln_file(self) -> Any:
        ...

    def to_vulns(self, raw: Any, ignore: PatchedIgnore) -> list[VulnFile]:
        ...


class SemgrepVulnProvider:
    SEMGREP_CWE_REGEX = r"CWE-(\d+)"

    def __init__(self, path: str | pathlib.Path, vuln_file: str | pathlib.Path | None = None):
        self._path = path
        self._vuln_file = vuln_file

    def _find_cwe(self, text: str) -> Cwe | None:
        match = re.search(self.SEMGREP_CWE_REGEX, text)
        if match is None:
            return None

        try:
            return Cwe(id=int(match.group(1)), title=text)
        except Exception as e:
            return None

    def run_provider(self, ignore: PatchedIgnore) -> list[VulnFile]:
        raw = self.read_vuln_file()
        if raw is None:
            raw = self.run_tool()

        return self.to_vulns(raw, ignore)

    def run_tool(self) -> Any:
        cmd = [
            "semgrep",
            "--config",
            "auto",
            "--config",
            "p/python",
            self._path,
            "--json",
        ]
        p = subprocess.run(cmd, capture_output=True, text=True)
        return json.loads(p.stdout)

    def read_vuln_file(self) -> Any:
        if self._vuln_file is None:
            return None
        with open(self._vuln_file, "r") as f:
            return json.load(f)

    def to_vulns(self, raw: dict, ignore: PatchedIgnore) -> list[VulnFile]:
        semgrep_result = raw["results"]

        path_vuln_metas = defaultdict(list)
        for result in semgrep_result:
            path = result["path"]
            if ignore.is_ignored(path):
                continue

            try:
                cwe = result["extra"]["metadata"]["cwe"]
            except KeyError:
                continue

            if isinstance(cwe, list):
                inner = []
                for cwe_element in cwe:
                    severity = SemgrepSeverity.from_str(result["extra"]["severity"])
                    cwe_obj = self._find_cwe(cwe_element)
                    if severity is None or cwe_obj is None:
                        continue
                    vuln_meta = Vuln(
                        cwe=cwe_obj,
                        severity=severity.value,
                        bug_msg=result["extra"]["message"],
                        start=result["start"]["line"],
                        end=result["end"]["line"],
                    )
                    inner.append(vuln_meta)
            else:
                severity = SemgrepSeverity.from_str(result["extra"]["severity"])
                cwe_obj = self._find_cwe(cwe)
                if severity is None or cwe_obj is None:
                    continue
                vuln_meta = Vuln(
                    cwe=cwe_obj,
                    severity=severity.value,
                    bug_msg=result["extra"]["message"],
                    start=result["start"]["line"],
                    end=result["end"]["line"],
                )
                inner = [vuln_meta]
            path_vuln_metas[result["path"]].extend(inner)

        vulns = []
        for path, vuln_metas in path_vuln_metas.items():
            with open(path, "r") as src_file:
                src = src_file.read()
            vuln = VulnFile(path=path, src=src, vulns=vuln_metas)
            vulns.append(vuln)
        return vulns


class SonarVulnProvider:
    def __init__(
        self,
        repo_dir: pathlib.Path,
        project_key: str,
        *,
        access_token: str | None = None,
        url: str = SonarClient.DEFAULT_URL,
        client: SonarClient | None = None,
    ):
        self._repo_dir = repo_dir
        self._project_key = project_key
        self._client = client or SonarClient(access_token, url)  # type: ignore

    def run_provider(self, ignore: PatchedIgnore) -> Any:
        raw = self.run_tool()
        return self.to_vulns(raw, ignore)

    def run_tool(self) -> Any:
        path_vulns = self._client.find_vulns(self._project_key)
        return path_vulns

    def read_vuln_file(self) -> Any:
        pass

    def to_vulns(self, raw: dict, ignore: PatchedIgnore) -> list[VulnFile]:
        vuln_files = []
        for path, vulns in raw.items():
            file_path = self._repo_dir / path
            if ignore.is_ignored(file_path):
                continue

            src = file_path.read_text()
            vuln_file = VulnFile(path=path, src=src, vulns=vulns)
            vuln_files.append(vuln_file)
        return vuln_files
