# Google Play Download Proxy

GPDP uses the Google Play API to generate HTML files with the application info, bridging the gap between [Obtainium](https://obtainium.imranr.dev/) and the Play Store.

When downloading an app, GPDP retreives the (split) APK and OBB files, packs them into an XAPK file on the fly, and forwards it to the client. No files are stored in memory or on the disk, which allows obtaining large apps on limited system resources

The developers are not affiliated with Google in any way.

GPDP is meant to be run on an Android device using Termux, or self-hosted otherwise. There is no public instance. There will be no public instance by me.

An instance of GPDP is designed to run using one Google account and one device configuration. Using multiple accounts or multiple device configurations requires running multiple instances.

## Web app

Using the web app to add an application to Obtainium is highly recommended, as the default Obtainium options will not recognize GPDP. This is an Obtainium limitation, and this is why the web app features an **Add to Obtainium** button for a two-click\* setup.

\*depending on your browser and browser settings

## Self-host

See **Running** to get started.

GPDP is not meant to be directly exposed to the Internet. Using a reverse proxy is highly recommended if running on different device than Obtainium.

When configuring a reverse proxy, make sure to forward the `Host` header to GPDP, otherwise the Obtainium links will point to something like `127.0.0.1:8000`, which will not work from a different device

GPDP doesn't support authentication. You can configure a reverse proxy to do this

## Development setup

### Virtual environment

Setting up a virtual environment is highly recommended

```sh
python -m "venv" .venv
. .venv/bin/activate
```

### Installing the project

```sh
# Specify -e to enable hot reloading without installing again
pip install .                     # for just running
pip install -e ".[dev]"           # with development tools and types
pip install -e ".[dev,protobuf]"  # to develop setup.py & to remove the import error
```

This will generate the required `.py` and optional `.pyi` files from `.proto` files.

### Manual `.proto` generation

In case you need to generate the Python code from `.proto` files manually

```sh
pip install ".[protobuf]"
python setup.py generate_protos
```

### Dispenser cache for development

GPDP will get a token from the configured dispenser on startup.
To reduce the number of requests towards the dispenser, and consequently, Google, especially when auto reload is enabled, run a cached dispenser and set `dispenser.url` to it in `gpdp.properties`

```sh
python scripts/cached_dispenser.py DISPENSER_URL DEVICE_PROPERTIES
HOST=127.0.0.1 PORT=3000 python scripts/cached_dispenser.py ...  # explicit host and port
```

This script queries the dispenser listening at `DISPENSER_URL` at startup, and serve its response until it is stopped

## Building

You can install `build` in a virtual environment.

```sh
# 1. Install build frontend
pip install build

# 2. Build project
pip -m build
pip -m build --wheel  # only wheel
```

## Running

1. Set up and run an [Aurora Dispenser](https://github.com/opekope2/aurora-dispenser). Set `dispenser.url` to it in `gpdp.properties`. Using a burner account is recommended  
    Replacing Aurora Dispenser with first-party authentication is planned. This is required till then
2. Run `uvicorn gpdp.server:app`. See [Uvicorn settings](https://uvicorn.dev/settings/) for more options

### Docker

GPDP is published to GHCR.
An example `compose.yml` file is provided in this repository.
It takes care of Aurora Dispenser. You only need to supply the config files

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
