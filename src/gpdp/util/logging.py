import json
import logging.config
import os

ENV_LOGGING_CONF = "GPDP_LOGGING_CONF"
DEFAULT_LOGGING_CONF = "logging.json"


def setup():
    logging_conf = os.getenv(ENV_LOGGING_CONF, DEFAULT_LOGGING_CONF)
    with open(logging_conf, encoding="utf-8") as logging_json:
        logging.config.dictConfig(json.load(logging_json))
