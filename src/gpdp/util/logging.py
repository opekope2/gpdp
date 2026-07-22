import functools
import json
import logging
import logging.config
import os
import sys
from collections.abc import Callable, Mapping
from copy import copy
from http import HTTPStatus
from logging import Logger, LogRecord
from typing import Concatenate, Literal, ParamSpec, Protocol, TypeVar, override

from uvicorn import _ansi
from uvicorn.logging import AccessFormatter, ColourizedFormatter

ENV_LOGGING_CONF = "GPDP_LOGGING_CONF"
DEFAULT_LOGGING_CONF = "logging.json"

PKG = "package"
STATUS = "status_code"


def setup():
    logging_conf = os.getenv(ENV_LOGGING_CONF, DEFAULT_LOGGING_CONF)
    with open(logging_conf, encoding="utf-8") as logging_json:
        logging.config.dictConfig(json.load(logging_json))


def get_logger(self: object):
    return logging.getLogger(
        f"{self.__class__.__module__}.{self.__class__.__qualname__}"
    )


class HasLogger(Protocol):
    logger: Logger


P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T", bound=HasLogger)


def log_info(msg: str):
    def decorator(func: Callable[Concatenate[T, P], R]):
        @functools.wraps(func)
        def wrapper(self: T, *args: P.args, **kwargs: P.kwargs):
            self.logger.info("%s", msg)
            return func(self, *args, **kwargs)

        return wrapper

    return decorator


def package_request_info(msg: str):
    def decorator(func: Callable[Concatenate[T, str, P], R]):
        @functools.wraps(func)
        def wrapper(self: T, pkg: str, *args: P.args, **kwargs: P.kwargs):
            self.logger.info("%s", msg, extra={PKG: pkg})
            return func(self, pkg, *args, **kwargs)

        return wrapper

    return decorator


class ColorfulFormatter(ColourizedFormatter):
    def __init__(
        self,
        fmt: str | None = None,
        datefmt: str | None = None,
        style: Literal["%", "{", "$"] = "%",
        use_colors: bool | None = None,
        extra_colors: Mapping[str, str | None] = {},
    ):
        self.extra_colors = extra_colors
        super().__init__(fmt=fmt, datefmt=datefmt, style=style, use_colors=use_colors)

    @override
    def should_use_colors(self):
        return sys.stderr.isatty()  # pragma: no cover

    def get_status(self, status_code: int):
        try:
            return f"{status_code} {HTTPStatus(status_code).phrase}"
        except ValueError:
            return str(status_code)

    def format_status(self, status_code: int, status: str):
        func = AccessFormatter.status_code_colours.get(
            status_code // 100, lambda _: status
        )
        return func(status)

    @override
    def formatMessage(self, record: LogRecord):
        if not self.use_colors:
            return super().formatMessage(record)

        record = copy(record)
        status_code = 0
        if hasattr(record, STATUS):
            status_code = getattr(record, STATUS)
            setattr(record, STATUS, self.get_status(status_code))

        if hasattr(record, STATUS) and not self.extra_colors.get(STATUS, None):
            status = getattr(record, STATUS)
            setattr(record, STATUS, self.format_status(status_code, status))

        for extra, fg in self.extra_colors.items():
            if not hasattr(record, extra):
                setattr(record, extra, "")
            else:
                setattr(record, extra, _ansi.style(getattr(record, extra), fg=fg))

        return super().formatMessage(record)
