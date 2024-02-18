from typing import Literal

from git import Repo

from patched_cli.client.patched import PatchedClient
from patched_cli.client.sonar import SonarClient
from patched_cli.git_helpers.git_helpers import get_slug_from_remote_url
from patched_cli.models.common import VulnFile
from patched_cli.models.records import LocalRepository
from patched_cli.scan.vuln_provider import (
    SemgrepVulnProvider,
    SonarVulnProvider,
    VulnProviderProtocol,
)
from patched_cli.scan.formats import SarifFormat
from patched_cli.utils.logging import logger
from patched_cli.utils.ignore import PatchedIgnore



def apply_flow(
    local_repository: LocalRepository,
    semgrep_vuln_file: str | None,
    sonar_project_key: str | None,
    sonar_client: SonarClient | None,
    client: PatchedClient,
) -> list[VulnFile]:
    vuln_provider: VulnProviderProtocol
    if sonar_client is not None and (local_repository.remote_url is not None or sonar_project_key is not None):
        logger.info("Using SonarQube as vulnerability provider")
        # sonar
        if sonar_project_key is None:
            slug = get_slug_from_remote_url(local_repository.remote_url)  # type: ignore
            project_key = slug.replace("/", "_")
        else:
            project_key = sonar_project_key

        vuln_provider = SonarVulnProvider(local_repository.path, project_key, client=sonar_client)
    elif semgrep_vuln_file is not None:
        try:
            vuln_files = SarifFormat().parse(local_repository.path, semgrep_vuln_file);
            return vuln_files
        except Exception as e:
            logger.exception(e)
            pass

        logger.info("Using Semgrep json file as vulnerability provider")
        # semgrep vuln file
        vuln_provider = SemgrepVulnProvider(local_repository.path, semgrep_vuln_file)
    else:
        logger.info("Using Semgrep as vulnerability provider")
        # default
        vuln_provider = SemgrepVulnProvider(local_repository.path)

    return vuln_provider.run_provider(PatchedIgnore(local_repository.path))
