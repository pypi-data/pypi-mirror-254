import configparser
import os
from typing import Any, Optional
from urllib.parse import urlparse

import click
from click import Context, Parameter
from click.core import ParameterSource

from patched_cli import envvars
from patched_cli.client.patched import PatchedClient
from patched_cli.client.scm import GithubClient, GitlabClient
from patched_cli.client.sonar import SonarClient
from patched_cli.utils.logging import logger
from patched_cli.utils.managed_files import CONFIG_FILE, HOME_FOLDER

_OPEN_COUNT = 0


def trigger_browser() -> None:
    global _OPEN_COUNT
    if _OPEN_COUNT < 1:
        _OPEN_COUNT = _OPEN_COUNT + 1
        click.launch(PatchedClient.TOKEN_URL)


class _NotSet:
    """
    Mainly used to indicate None without using NoneType just so that the prompt is handled on our end,
    rather than on click.
    """

    def __init__(self):
        pass


class UrlParamType(click.ParamType):
    name = ""

    def convert(self, value, param, ctx):
        try:
            urlparse(value)
            return value
        except ValueError:
            self.fail(f"{value} is not a valid URL", param, ctx)


class PatchedClientParamType(click.ParamType):
    name = ""

    def convert(self, value: Any, param: Optional["Parameter"], ctx: Optional["Context"]) -> PatchedClient:
        if ctx is None or param is None or param.name is None:
            raise ValueError("Unhandled usage of type")

        url = os.environ.get(envvars.PATCH_URL_ENVVAR, PatchedClient.DEFAULT_PATCH_URL)
        source = ctx.get_parameter_source(param.name)

        # value can be either str, PatchedClient or _NotSet
        client = None
        if isinstance(value, str):
            client = PatchedClient(url, value)
        elif isinstance(value, PatchedClient):
            client = value

        if client is not None and client.test_token():
            return client

        if client is None:
            current_value = click.prompt(
                f'Opening login at: "{PatchedClient.TOKEN_URL}".\n'
                "Please go to the Integration's tab and generate an API key.\n"
                "Please copy the access token that is generated, "
                "paste it into the terminal and press the return key.\n"
                "Token",
                hide_input=True,
            )
            client = PatchedClient(url, current_value)
            if client.test_token():
                return client

            for _ in range(2):
                current_value = click.prompt(
                    "Invalid access token. Please try again.\n" "Access Token",
                    hide_input=True,
                )
                client = PatchedClient(url, current_value)
                if client.test_token():
                    return client
            logger.error("Access Token rejected too many times. Please verify that access token is correct.")
            ctx.abort()

        if source == ParameterSource.DEFAULT:
            logger.error(
                f'Access Token rejected from file "{CONFIG_FILE}".\n'
                f"Please verify that the access token is correct or delete the file."
            )
            ctx.abort()

        if source == ParameterSource.ENVIRONMENT:
            logger.error(
                f"\n"
                f'Access Token rejected from "{param.envvar}" environment variable.\n'
                f"Please verify that the access token is correct."
            )
            ctx.abort()

        self.fail(f"Access Token rejected. Please verify that the access token is correct.")

    @staticmethod
    def default() -> str | _NotSet:
        HOME_FOLDER.mkdir(exist_ok=True)

        if not CONFIG_FILE.exists():
            trigger_browser()
            return _NotSet()

        parser = configparser.ConfigParser()
        parser.read(CONFIG_FILE)
        if "patched" not in parser:
            trigger_browser()
            return _NotSet()

        if "access.token" not in parser["patched"]:
            trigger_browser()
            return _NotSet()

        return parser["patched"]["access.token"]

    @staticmethod
    def callback(ctx, param, value: PatchedClient) -> PatchedClient:
        HOME_FOLDER.mkdir(exist_ok=True)
        CONFIG_FILE.touch(exist_ok=True)

        parser = configparser.ConfigParser()
        parser.read(CONFIG_FILE)

        is_changed = False
        if "patched" not in parser:
            parser.add_section("patched")
            is_changed = True
        if "access.token" not in parser["patched"]:
            parser["patched"] = {"access.token": value.access_token}
            is_changed = True

        if is_changed:
            with open(CONFIG_FILE, "w") as fp:
                parser.write(fp)

        return value


class GithubClientParamType(click.ParamType):
    name = ""

    def convert(self, value: Any, param: Optional["Parameter"], ctx: Optional["Context"]) -> GithubClient:
        return GithubClient(access_token=value)


class GitlabClientParamType(click.ParamType):
    name = ""

    def convert(self, value: Any, param: Optional["Parameter"], ctx: Optional["Context"]) -> GitlabClient:
        return GitlabClient(access_token=value)


class SonarClientParamType(click.ParamType):
    name = ""

    def convert(self, value: Any, param: Optional["Parameter"], ctx: Optional["Context"]) -> SonarClient:
        return SonarClient(access_token=value)
