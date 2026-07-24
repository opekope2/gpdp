#!/usr/bin/env python3

from pathlib import Path

import grpc_tools.protoc

ROOT = Path(__file__).parent.parent
PROTO_DIR = ROOT / "protos"
OUT_DIR = ROOT / "src" / "gpdp" / "proto"


def main():
    protos = [str(path.relative_to(PROTO_DIR)) for path in PROTO_DIR.rglob("*.proto")]

    args = [
        "grpc_tools.protoc",
        f"-I{PROTO_DIR}",
        f"--python_out={OUT_DIR}",
        f"--pyi_out={OUT_DIR}",
        *protos,
    ]
    result = grpc_tools.protoc.main(args)
    if result != 0:
        raise SystemExit(result)


if __name__ == "__main__":
    main()
