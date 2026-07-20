# Google Play Download Proxy

## Running

Run `uvicorn gpdp.server:app`

## Stubs

`googleplay-api` doesn't ship with `.pyi` files, making IntelliSense unusable.
For this reason, this repo contains `stubs/gpapi/googleplay_pb2.pyi`, which was generated using `protoc --pyi_out=stubs/gpapi googleplay.proto`.
