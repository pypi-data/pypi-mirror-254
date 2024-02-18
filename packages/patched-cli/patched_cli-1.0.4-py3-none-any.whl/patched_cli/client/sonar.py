from collections import defaultdict

import requests

from patched_cli.models.common import Vuln, Severity, Cwe
from patched_cli.utils.logging import logger


class SonarClient:
    DEFAULT_URL = "https://sonarcloud.io/api"
    __token_search_path = "/user_tokens/search"
    __issue_path = "/issues/search"
    __hotspot_path = "/hotspots/search"
    __hotspot_details_path = "/hotspots/show"

    def __init__(self, access_token: str, url: str = DEFAULT_URL) -> None:
        self._access_token = access_token
        self._url = url

    def set_url(self, url: str) -> None:
        self._url = url

    def test_token(self) -> bool:
        headers = {"Authorization": f"Bearer {self._access_token}"}
        response = requests.get(self._url + self.__token_search_path, headers=headers)
        return response.ok

    def find_vulns(self, project_key: str) -> dict[str, list[Vuln]]:
        rv = defaultdict(list)
        for hotspot in self._find_hotspots(project_key):
            hotspot_details = self._find_hotspot_details(hotspot["key"])
            if hotspot_details is None:
                continue

            try:
                path = hotspot_details["component"]["path"]
                title = hotspot_details["rule"]["name"]
                bug_msg = hotspot_details["rule"]["riskDescription"]
                start = hotspot_details["textRange"]["startLine"]
                end = hotspot_details["textRange"]["endLine"]
            except KeyError:
                logger.warning(f"Malformed hotspot details response for {hotspot['component']}")
                continue

            vuln = Vuln(
                severity=Severity.CRITICAL,
                cwe=Cwe(id=-1, title=title),
                bug_msg=bug_msg,
                start=start,
                end=end,
            )

            rv[path].append(vuln)

        return rv

    def _find_hotspot_details(self, hotspot_key: str) -> dict | None:
        headers = {"Authorization": f"Bearer {self._access_token}"}
        # Define the parameters for Hotspot API request
        params: dict[str, str | int] = {"hotspot": hotspot_key}
        url = self._url + self.__hotspot_details_path
        response = requests.get(url, params=params, headers=headers)
        if not response.ok:
            print("Something went wrong with sonar hotspot details API:", response.text)
            return None

        return response.json()

    def _find_hotspots(self, project_key: str):
        page = 1
        page_size = 50

        headers = {"Authorization": f"Bearer {self._access_token}"}
        # Define the parameters for Hotspot API request
        params: dict[str, str | int] = {
            "p": page,
            "ps": page_size,
            "projectKey": project_key,
            "status": "TO_REVIEW",
        }

        url = self._url + self.__hotspot_path

        is_done = False
        while not is_done:
            response = requests.get(url, params=params, headers=headers)
            if not response.ok:
                print("Something went wrong with hotspot API:", response.text)
                return

            data = response.json()
            hotspots = data["hotspots"]

            is_done = len(hotspots) < page_size
            params["p"] = int(params["p"]) + 1

            for hotspot in hotspots:
                yield hotspot

    # unused
    def find_issues(self, project_key: str):
        page = 1
        page_size = 50

        headers = {"Authorization": f"Bearer {self._access_token}"}

        params: dict[str, str | int] = {
            "p": page,
            "ps": page_size,
            "project": project_key,
            "status": "VULNERABILITY",
            "impactSoftwareQualities": "SECURITY",
        }

        url = self._url + self.__issue_path

        is_done = False
        while not is_done:
            # Send the API request for sonar results
            response = requests.get(url, params=params, headers=headers)
            if not response.ok:
                print("Something went wrong with sonar issues API")
                return

            data = response.json()
            is_done = len(data["issues"]) < page_size
            params["p"] = int(params["p"]) + 1

            # maps to prefix of issue.project
            component_by_key = {
                component["key"]: component
                for component in data["components"]
                if component["qualifier"] == "FIL" and "path" in component.keys()
            }
            # maps to issue.rule
            rule_by_key = {rule["key"]: rule for rule in data["rules"]}

            for issue in data["issues"]:
                issue_component_key = next(
                    (key for key in component_by_key.keys() if key.startswith(issue["key"])),
                    None,
                )
                rule = rule_by_key.get(issue["rule"], None)
                if issue_component_key is None or rule is None:
                    continue

                severity = Severity(issue["impacts"]["severity"])

                path = component_by_key[issue_component_key]["path"]
                vuln = Vuln(
                    cwe=Cwe(id=-1, title=issue["message"]),
                    severity=severity,
                    bug_msg=rule["name"],
                    start=issue["textRange"]["startLine"],
                    end=issue["textRange"]["endLine"],
                )
                yield path, vuln
