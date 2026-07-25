# Google Play Download Proxy

## Development setup

1. Set up a [virtual environment](https://docs.python.org/3/library/venv.html) using `python -m venv .venv`
2. Activate the virtual environment using `. .venv/bin/activate`
3. Install the project using `pip install -e ".[dev]"`
4. Run `scripts/generate_protos.py` to generate the needed Protobuf files

## Dispenser cache

GPDP will get a token from the configured dispenser on startup.
To reduce the number of requests towards the dispenser, and consequently, Google, especially when auto reload is enabled, run a cached dispenser and set it in `config.properties`: `scripts/cached_dispenser.py [DISPENSER_URL] [DEVICE_PROPERTIES]`. This will query the dispenser located at `[DISPENSER_URL]` at startup, and serve its response until it is stopped.
Optionally specify the `HOST` and/or `PORT` environment variables.

## Building

Run `python -m build`

## Running

Set up and run an [Aurora Dispenser](https://gitlab.com/AuroraOSS/aurora-dispenser). Set its url in `gpdp.properties`

Run `uvicorn gpdp.server:app`. See [Uvicorn settings](https://uvicorn.dev/settings/) for more options.

### Environment variables

#### `GPDP_CONF`

Path to GPDP configuration.
Defaults to `gpdp.properties`

#### `GPDP_DEVICE_CONF`

Path to the device configuration. Export your device configuration using [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore)'s Spoof Manager or get one from [Aurora Config Generator](https://auroraoss.com/config-generator).
Defaults to `device.properties`

#### `GPDP_LOGGING_CONF`

Path to GPDP logging configuration.
See [Logging configuration](https://docs.python.org/3/library/logging.config.html#logging-config-dictschema).
Defaults to `logging.json`

### GPDP configuration (`gpdp.properties`)

#### `dispenser.url`

The API endpoint of the token dispenser. **Do not use `auroraoss.com`** as it's reserved for Aurora Store users, and you'll probably get blocked by Cloudflare anyway. Self-host your own.

#### `dispenser.refresh_cooldown`

GPDP will try to refresh the token using the token dispenser if Google Play returns `401 Unauthorized`. GPDP will not try to refresh the token within this many seconds of the previous attempt (in case it fails).

#### `obtainium.auto_add`

If set to true, GPDP will try to automatically add the apps to Obtainium if viewed from a browser (no JavaScript).

#### `play.download.compressed`

If set to true, GPDP will download compressed files from Google Play and decompress them on the fly before packaging it into an XAPK.

#### `play.locale.default`

The fallback language to use for Google Play queries.
Used when the client doesn't specify an `Accept-Language` header.

## Acknowledgements

This project was heavily inspired by [gplay-apk-downloader](https://github.com/alltechdev/gplay-apk-downloader)

[GPlayApi](https://gitlab.com/AuroraOSS/gplayapi) for Google Play `.proto` files

[Aurora Dispenser](https://gitlab.com/AuroraOSS/aurora-dispenser) for authentication so this project doesn't have to on its own
