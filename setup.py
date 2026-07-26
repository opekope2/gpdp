from pathlib import Path
from typing import override

import grpc_tools.protoc
import setuptools
from setuptools.command.build_py import build_py

ROOT = Path(__file__).parent
PROTO_DIR = ROOT / "src" / "protos"
OUT_DIR = ROOT / "src" / "gpdp" / "proto"


def generate_protos():
    PROTO_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

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
        raise RuntimeError(f"protoc failed with code {result}")


class BuildPy(build_py):
    @override
    def run(self):
        generate_protos()
        super().run()


class GenerateProtos(setuptools.Command):
    description = "generate python code from .proto files"

    @override
    def initialize_options(self):
        pass

    @override
    def finalize_options(self):
        pass

    @override
    def run(self):
        generate_protos()


setuptools.setup(
    cmdclass={
        "build_py": BuildPy,
        "generate_protos": GenerateProtos,
    }
)
