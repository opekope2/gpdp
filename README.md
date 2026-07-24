# Google Play Download Proxy

## Development setup

1. Set up a [virtual environment](https://docs.python.org/3/library/venv.html) using `python -m venv .venv`
2. Activate the virtual environment using `. .venv/bin/activate`
3. Install the project using `pip install -e ".[dev]"`
4. Run `scripts/generate_protos.py` to generate the needed Protobuf files

## Running

Run `uvicorn gpdp.server:app`

### Environment variables

#### `GPDP_LOGGING_CONF`

Path to `logging.json`.
See [Logging configuration](https://docs.python.org/3/library/logging.config.html#logging-config-dictschema).

Defaults to `logging.json`
