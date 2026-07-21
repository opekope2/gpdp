import json
import logging
import logging.config
import os

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
