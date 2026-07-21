# Google Play Download Proxy

## Running

Run `uvicorn gpdp.server:app`

### Environment variables

#### `GPDP_LOGGING_CONF`

Path to `logging.json`.
See [Logging configuration](https://docs.python.org/3/library/logging.config.html#logging-config-dictschema).

Defaults to `logging.json`

## Stubs

`googleplay-api` doesn't ship with `.pyi` files, making IntelliSense unusable.
For this reason, this repo contains `stubs/gpapi/googleplay_pb2.pyi`, which was generated using `protoc --pyi_out=stubs/gpapi googleplay.proto`.
