from pathlib import Path

import click

HOME_FOLDER = Path(click.get_app_dir("Patched", force_posix=True))
_CONFIG_NAME = "config.ini"
_LOG_NAME = "patched.log"
LOG_FILE = HOME_FOLDER / _LOG_NAME
CONFIG_FILE = HOME_FOLDER / _CONFIG_NAME

IGNORE_NAME = ".patchedignore"
