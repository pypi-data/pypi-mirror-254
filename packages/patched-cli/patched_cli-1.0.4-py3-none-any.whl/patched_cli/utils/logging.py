import logging
from typing import Callable

import click
import sentry_sdk

from patched_cli.utils.managed_files import LOG_FILE

# default noop logger
logger = logging.getLogger("patched_cli")
_noop = logging.NullHandler()
logger.addHandler(_noop)


class ClickHandler(logging.Handler):
    def __init__(self, is_debug: bool):
        super().__init__()
        self.addFilter(self._get_filter(is_debug))

    def emit(self, record: logging.LogRecord) -> None:
        kwargs = {}
        message = record.message

        if record.levelno == logging.ERROR:
            kwargs["err"] = True
        elif record.levelno == logging.WARNING:
            message = click.style(record.message, bold=True)

        click.echo(message, **kwargs)

        if kwargs.get("err", False) and record.exc_info is not None:
            sentry_sdk.capture_exception(record.exc_info)

    def _get_filter(self, is_debug: bool) -> Callable[[logging.LogRecord], bool]:
        log_level = logging.DEBUG if is_debug else logging.INFO

        def inner(record: logging.LogRecord) -> bool:
            return record.levelno >= log_level

        return inner


def init_cli_logger(is_debug: bool) -> logging.Logger:
    global logger, _noop
    logger.removeHandler(_noop)

    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(LOG_FILE, mode="w")
    formatter = logging.Formatter("%(asctime)s :: %(filename)s@%(funcName)s@%(lineno)d :: %(levelname)s :: %(msg)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ClickHandler(is_debug))

    return logger
