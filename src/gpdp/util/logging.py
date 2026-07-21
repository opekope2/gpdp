import functools
import json
import logging
import logging.config
import os
from collections.abc import Callable
from logging import Logger
from typing import Any, Concatenate, ParamSpec, TypeVar

ENV_LOGGING_CONF = "GPDP_LOGGING_CONF"
DEFAULT_LOGGING_CONF = "logging.json"

PKG = "package"


def setup():
    logging_conf = os.getenv(ENV_LOGGING_CONF, DEFAULT_LOGGING_CONF)
    with open(logging_conf, encoding="utf-8") as logging_json:
        logging.config.dictConfig(json.load(logging_json))


def get_logger(self: object):
    return logging.getLogger(
        f"{self.__class__.__module__}.{self.__class__.__qualname__}"
    )


P = ParamSpec("P")
R = TypeVar("R")


def package_request_info(logger_getter: Callable[[Any], Logger], msg: str):
    def decorator(func: Callable[Concatenate[Any, str, P], R]):
        @functools.wraps(func)
        def wrapper(self: Any, pkg: str, *args: P.args, **kwargs: P.kwargs):
            logger_getter(self).info("%s", msg, extra={PKG: pkg})
            return func(self, pkg, *args, **kwargs)

        return wrapper

    return decorator
