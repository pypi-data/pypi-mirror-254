import json
import os
import pathlib

from urllib.parse import urlparse
from patched_cli.models.common import VulnFile, Vuln, Cwe
from patched_cli.models.enums import Severity
from patched_cli.utils.logging import logger


class SarifFormat:
    def parse(self, repo_path: pathlib.Path, vuln_file: str | pathlib.Path) -> list[VulnFile]:
        with open(vuln_file) as f:
            sarif_results = json.load(f)

        total_vuln_files = []
        for runs in sarif_results["runs"]:
            locations = []
            for artifact in runs["artifacts"]:
                uri = artifact["location"]["uri"]
                uri = urlparse(uri)
                path = uri.path
                path = path.lstrip("/")
                location = pathlib.Path(path)
                if not location.is_file():
                    # find by wildcard
                    location = next(pathlib.Path(repo_path).glob(f"**{os.sep}{path}"), None)
                if location is None:
                    # cut the first repo path and try to find the file again
                    path = path.lstrip(repo_path.name)
                    location = next(pathlib.Path(repo_path).glob(f"**{os.sep}{path}"), None)

                if location is None:
                    logger.warning(f"Unable to find file {path}")
                    continue
                locations.append(location)

            vuln_files: list[VulnFile | None] = [None for _ in locations]
            for result in runs["results"]:
                try:
                    result_location = result["locations"][0]
                    artifact_index = result_location["physicalLocation"]["artifactLocation"]["index"]

                    start_line = result_location["physicalLocation"]["region"]["startLine"]
                    location = locations[artifact_index]
                    bug_msg = result["message"]["text"]
                    severity = Severity.from_str(result["properties"]["Severity"])
                except KeyError as e:
                    continue
                except IndexError as e:
                    continue

                vuln = Vuln(
                    cwe=Cwe(id=-1, title=bug_msg),
                    severity=severity,
                    bug_msg=bug_msg,
                    start=start_line,
                    end=start_line,
                )

                vuln_file = vuln_files[artifact_index]
                if vuln_file is None:
                    if location is None:
                        continue
                    with open(location) as f:
                        src = f.read()

                    vuln_file = VulnFile(
                        path=str(location),
                        src=src,
                        vulns=[vuln],
                        is_obfuscated=False)
                    vuln_files[artifact_index] = vuln_file
                else:
                    vuln_file = vuln_files[artifact_index]
                    vuln_file.vulns.append(vuln)
            total_vuln_files.extend(vuln_files)
        return [total_vuln_files for total_vuln_files in total_vuln_files if total_vuln_files is not None]

