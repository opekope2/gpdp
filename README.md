# Google Play Download Proxy

## Development setup

1. Set up a [virtual environment](https://docs.python.org/3/library/venv.html) using `python -m venv .venv`
2. Activate the virtual environment using `. .venv/bin/activate`
3. Install the project using `pip install -e ".[dev]"`
4. Run `scripts/generate_protos.py` to generate the needed Protobuf files

## Development

GPDP will get a token from the configured dispenser on startup.
To reduce the number of requests towards the dispenser, run a cached dispenser and set it in `config.json`: `scripts/cached_dispenser.py [DISPENSER_URL] [DEVICE_PROPERTIES]`.
Optionally specify the `HOST` and/or `PORT` environment variables.

## Building

Run `python -m build`

## Running

Run `uvicorn gpdp.server:app`

### Environment variables

#### `GPDP_LOGGING_CONF`

Path to `logging.json`.
See [Logging configuration](https://docs.python.org/3/library/logging.config.html#logging-config-dictschema).

Defaults to `logging.json`

## Acknowledgements

This project was heavily inspired by [gplay-apk-downloader](https://github.com/alltechdev/gplay-apk-downloader)

[GPlayApi](https://gitlab.com/AuroraOSS/gplayapi) for Google Play `.proto` files

[Aurora Dispenser](https://gitlab.com/AuroraOSS/aurora-dispenser) for authentication so this project doesn't have to on its own
