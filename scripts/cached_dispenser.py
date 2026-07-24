#!/usr/bin/env python3

import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

from httpx import Client, codes

from gpdp.http.content_types import CONTENT_TYPE_JSON
from gpdp.http.headers import ACCEPT, CONTENT_LENGTH, CONTENT_TYPE
from gpdp.util import device


def create_handler(auth_bundle: bytes):
    class PostHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(codes.OK)

            self.send_header(CONTENT_TYPE, CONTENT_TYPE_JSON)
            self.send_header(CONTENT_LENGTH, str(len(auth_bundle)))
            self.end_headers()

            self.wfile.write(auth_bundle)

        def do_POST(self):
            self.do_GET()

    return PostHandler


def main(args: list[str]):
    if len(args) < 3:
        print(f"Usage: {args[0]} [DISPENSER_URL] [DEVICE_PROPERTIES]")
        raise SystemExit(1)

    dispenser_url = args[1]
    device_properties = args[2]
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "3000"))
    dev = device.load(device_properties)

    with Client() as http:
        print("Getting auth bundle from dispenser")
        res = http.post(
            dispenser_url,
            json=dev.model_dump(by_alias=True),
            headers={ACCEPT: CONTENT_TYPE_JSON, CONTENT_TYPE: CONTENT_TYPE_JSON},
        )
        res.raise_for_status()

    server = HTTPServer((host, port), create_handler(res.content))
    print(f"Serving auth bundle on {host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main(sys.argv)
