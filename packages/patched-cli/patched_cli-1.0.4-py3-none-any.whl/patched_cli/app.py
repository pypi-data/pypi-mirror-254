import atexit
from pathlib import Path

import click
import sentry_sdk
from click_option_group import MutuallyExclusiveOptionGroup, optgroup
from git import InvalidGitRepositoryError, Repo

from patched_cli.client.patched import PatchedClient
from patched_cli.client.scm import GithubClient, GitlabClient, ScmPlatformClientProtocol
from patched_cli.client.sonar import SonarClient
from patched_cli.git_helpers.git_helpers import create_branch_and_pr
from patched_cli.models.enums import Severity
from patched_cli.models.records import LocalRepository
from patched_cli.scan.common import apply_file_changes
from patched_cli.scan.filter import Filters
from patched_cli.scan.flow import apply_flow
from patched_cli.utils.click_param_types import (
    GithubClientParamType,
    GitlabClientParamType,
    PatchedClientParamType,
    SonarClientParamType,
    UrlParamType,
)
from patched_cli.utils.logging import init_cli_logger, logger
from patched_cli.utils.obfuscation import Obfuscator

sentry_sdk.init(
    dsn="https://851250f33454ef7fe75cdcdbc6ecaef5@o4506197015330816.ingest.sentry.io/4506221506134016",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

atexit.register(sentry_sdk.flush)


@click.command
@click.version_option(message="%(version)s")
@click.help_option("-h", "--help")
@click.argument(
    "path",
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    default=Path.cwd(),
)
@click.option(
    "patched_client",
    "-t",
    "--access-token",
    help="Patched Access Token, can be generated through https://app.patched.codes/signin -> Integrations. "
    'This can be set with environment variable "PATCHED_ACCESS_TOKEN".',
    envvar="PATCHED_ACCESS_TOKEN",
    required=True,
    type=PatchedClientParamType(),
    default=PatchedClientParamType.default,
    callback=PatchedClientParamType.callback,
)
@click.option(
    "is_create_pr",
    "-P",
    "--create-pr",
    help="Create a pull request. \n"
    "With the current branch as the base branch and the head branch as the patched branch.",
    is_flag=True,
    default=False,
    show_default=True,
)
@click.option(
    "is_non_git",
    "--non-git",
    help="Apply patches to a non-git local directory.",
    is_flag=True,
    default=False,
    show_default=True,
)
@click.option(
    "is_allow_dirty",
    "--dirty",
    help="Apply patches to a dirty git repository.",
    is_flag=True,
    default=False,
    show_default=True,
)
@click.option(
    "patch_current_branch",
    "--patch-current-branch",
    help="Apply patches to the current git repository.",
    is_flag=True,
    default=False,
    show_default=True,
)
@click.option(
    "vuln_report",
    "--vuln",
    help="Vulnerability Report based on flow.",
    type=click.Path(exists=True, file_okay=True, resolve_path=True, dir_okay=False),
)
@click.option(
    "validate",
    "--validate",
    help="Validate patch.",
    is_flag=True,
    default=False,
    show_default=True,
)
@click.option(
    "is_obfuscation_required",
    "--obfuscate",
    help="Obfuscate code locally before patching. Currently only supports Python. "
         "Code that fails to obfuscate will not be patched.",
    is_flag=True,
    default=False,
    show_default=True,
)
@click.option(
    "is_obfuscation_proof_required",
    "--save",
    help="Write the obfuscated code to disk before patching ",
    is_flag=True,
    default=False,
    show_default=True,
)
@click.option(
    "filters",
    "--filter",
    help="Filter vulnerabilities by severity, or CWE. e.g. --filter \"severity=high\" --filter \"cwe=123\". "
         f"Possible values for severity are {Severity.__members__.keys()}. This can be set multiple times.",
    multiple=True,
    default=[]
)
@click.option(
    "sonar_project_key",
    "--sonar-project-key",
    help="""
         Sonar's URL.
         This can be set with environment variable \"PATCHED_SONAR_PROJ_KEY\".
         """,
    envvar="PATCHED_SONAR_PROJ_KEY",
)
@click.option(
    "sonar_url",
    "--sonar-url",
    help="""
         Sonar's URL.
         This can be set with environment variable \"PATCHED_SONAR_URL\".
         """,
    envvar="PATCHED_SONAR_URL",
    type=UrlParamType(),
    default=SonarClient.DEFAULT_URL,
    show_default=True,
)
@click.option(
    "sonar_client",
    "--sonar-token",
    help="""
         Sonar's Access Token, can be generated from \"https://sonarcloud.io/account/security\".
         This can be set with environment variable \"PATCHED_SONAR_TOKEN\". 
         """,
    envvar="PATCHED_SONAR_TOKEN",
    type=SonarClientParamType(),
)
@click.option(
    "platform_url",
    "--platform-url",
    help="SCM Platform's URL. "
    f'Default value for Github is "{GithubClient.DEFAULT_URL}". '
    f'Default value for Gitlab is "{GitlabClient.DEFAULT_URL}". ',
    envvar="PATCHED_SCM_PLATFORM_URL",
    type=UrlParamType(),
)
@optgroup(cls=MutuallyExclusiveOptionGroup)
@optgroup.option(
    "github_client",
    "--github-access-token",
    help="""
        Github's Personal Access Token, can be generated from \"https://github.com/settings/tokens\". 
        This can be set with environment variable \"PATCHED_GITHUB_TOKEN\".
        """,
    envvar="PATCHED_GITHUB_TOKEN",
    type=GithubClientParamType(),
)
@optgroup.option(
    "gitlab_client",
    "--gitlab-access-token",
    help="""
         Gitlab's Personal Access Token, can be generated from \"https://gitlab.com/-/profile/personal_access_tokens\".
         This can be set with environment variable \"PATCHED_GITLAB_TOKEN\". 
         """,
    envvar="PATCHED_GITLAB_TOKEN",
    type=GitlabClientParamType(),
)
@click.option(
    "is_debug",
    "--debug",
    is_flag=True,
    type=bool,
    default=False,
    hidden=True,
)
def main(
    path: str,
    patched_client: PatchedClient,
    platform_url: str | None,
    github_client: GithubClient | None,
    gitlab_client: GitlabClient | None,
    is_create_pr: bool,
    is_non_git: bool,
    is_allow_dirty: bool,
    patch_current_branch: bool,
    vuln_report: str | None,
    sonar_project_key: str | None,
    sonar_url: str,
    sonar_client: SonarClient | None,
    validate: bool,
    is_obfuscation_required: bool,
    is_obfuscation_proof_required: bool,
    filters: list[str],
    is_debug: bool,
):
    init_cli_logger(is_debug)

    platform_client: ScmPlatformClientProtocol | None = github_client or gitlab_client
    local_repository = _validations(
        is_allow_dirty=is_allow_dirty,
        is_non_git=is_non_git,
        patch_current_branch=patch_current_branch,
        is_obfuscation_required=is_obfuscation_required,
        is_obfuscation_proof_required=is_obfuscation_proof_required,
        path=path,
        platform_client=platform_client,
        platform_url=platform_url,
        sonar_client=sonar_client,
        sonar_url=sonar_url,
    )

    try:
        vuln_filter = Filters.from_str_list(filters)
    except ValueError as e:
        logger.error(e)
        exit(1)

    vuln_files = apply_flow(local_repository, vuln_report, sonar_project_key, sonar_client, patched_client)
    vuln_files = [vuln_file for vuln_file in vuln_filter.apply_vuln_file(vuln_files)]
    if len(vuln_files) == 0:
        logger.info("No vulnerabilities found.")
        exit(0)

    for vuln_file in vuln_files:
        logger.info(f"Found {len(vuln_file.vulns)} Vulnerabilities at {vuln_file.path}")
    vuln_count = sum(len(vuln_file.vulns) for vuln_file in vuln_files)

    obsfucators = {}
    if is_obfuscation_required:
        logger.info("Obfuscating code.....")
        for i, vuln_file in enumerate(vuln_files):
            obfuscator = Obfuscator()
            try:
                vuln_file.src = obfuscator.obfuscate(vuln_file.src)
                # try deobfuscating to make sure it works
                obfuscator.deobfuscate(vuln_file.src)
                vuln_file.is_obfuscated = True
                obsfucators[vuln_file.path] = obfuscator
            except Exception as e:
                sentry_sdk.capture_exception(e)
                logger.error(f"Error while obfuscating {vuln_file.path}")
                del vuln_files[i]

        logger.info("Obfuscated!")

        if is_obfuscation_proof_required:
            for vuln_file in vuln_files:
                vuln_file_path = Path(vuln_file.path)
                obfuscated_file = vuln_file_path.with_name(f"{vuln_file_path.stem}_obfuscated{vuln_file_path.suffix}")
                obfuscated_file.write_text(vuln_file.src)

    logger.info("Begin generating patches.....")
    try:
        patch_response = patched_client.get_patches(local_repository.path, local_repository.repo, vuln_files)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        logger.error(f"Unexpected error: {e}", exc_info=e)
        exit(1)

    report = patch_response.report

    logger.debug(f"Vulnerabilities Found : {report.vulns_found}")
    if is_obfuscation_required:
        obfuscation_count = sum(len(vuln_file.vulns) for vuln_file in vuln_files if vuln_file.is_obfuscated)
        logger.info(f"In Obfuscated Files: {obfuscation_count}")
    logger.debug(f"Vulnerabilities Triaged: {report.vulns_triaged}")
    logger.debug(f"Fixes Generated : {report.fixes_generated}")
    logger.debug(f"Fixes Validated : {report.fixes_triaged}")

    patches = patch_response.patches
    if len(patches) < 1:
        logger.info(f"No patches generated")
        exit(0)

    if is_obfuscation_required:
        logger.info("Deobfuscating patches.....")
        for i, patch in enumerate(patches):
            try:
                patch.patch = obsfucators[patch.path].deobfuscate(patch.patch)
            except Exception as e:
                sentry_sdk.capture_exception(e)
                logger.error(f"Error while deobfuscating {patch.path}")
                del patches[i]
        logger.info("Deobfuscated!")

    logger.info("Applying patches.....")
    changed_files = apply_file_changes(path, patches)
    if len(changed_files) < 1 or (local_repository.repo is not None and len(local_repository.repo.git.diff()) < 1):
        logger.info("No files patched!")
        exit(0)
    logger.info("Patched!")

    if validate and sonar_client is None:
        new_vuln_files = apply_flow(
            local_repository,
            vuln_report,
            sonar_project_key,
            sonar_client,
            patched_client,
        )
        new_vuln_count = sum(len(vuln_file.vulns) for vuln_file in new_vuln_files)
        percent = (1 - new_vuln_count / vuln_count) * 100
        logger.info(f"Fixed {round(percent, 2)}% vulnerabilities")

    if local_repository.repo is not None:
        result = create_branch_and_pr(
            local_repository,
            changed_files,
            is_create_pr,
            platform_client,
            patched_client,
        )
        logger.info(result.message)


def _validations(
    is_allow_dirty: bool,
    is_non_git: bool,
    patch_current_branch: bool,
    is_obfuscation_required: bool,
    is_obfuscation_proof_required: bool,
    path: str,
    platform_client: ScmPlatformClientProtocol | None,
    platform_url: str | None,
    sonar_client: SonarClient | None,
    sonar_url: str,
) -> LocalRepository:
    repo = None
    try:
        repo = Repo(path)
    except InvalidGitRepositoryError:
        if not is_non_git:
            logger.error(
                f'Path: "{path}" is not a git repository. '
                f'To patch a non-git local repository, please use the "--non-git" flag.')
            exit(1)

    local_repo = LocalRepository(Path(path), repo, not patch_current_branch)

    if not is_allow_dirty and repo is not None and repo.is_dirty(untracked_files=True):
        logger.error(
            f'Path: "{path}" is a git repository, but it is dirty. '
            f'To patch a dirty git repository, please use the "--dirty" flag.')
        exit(1)

    # TODO: remove this side effect
    if platform_client is not None and platform_url is not None:
        platform_client.set_url(platform_url)

    if sonar_client is not None and sonar_url is not None:
        sonar_client.set_url(sonar_url)

    if sonar_client is not None and not sonar_client.test_token():
        logger.error(f'Unable to access Sonar at "{sonar_url}" with provided token.')
        exit(1)

    if platform_client is not None and not platform_client.test():
        logger.error(f'Unable to access SCM Platform at "{platform_url}" with provided token.')
        exit(1)

    if is_obfuscation_proof_required and not is_obfuscation_required:
        logger.error(f'Cannot write obfuscated code to disk without obfuscating it. '
                     f'Please use the "--obfuscation" flag.')
        exit(1)

    # TODO: remove this return
    return local_repo


if __name__ == "__main__":
    main()
