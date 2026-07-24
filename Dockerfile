FROM python:slim AS builder

WORKDIR /build

COPY . .

ENV PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_ROOT_USER_ACTION=ignore

RUN pip install build grpcio-tools && mkdir -p src/gpdp/proto && python scripts/generate_protos.py && python -m build --wheel

FROM python:slim AS runtime

WORKDIR /app

COPY --from=builder /build/dist/*.whl /tmp/

ENV PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_ROOT_USER_ACTION=ignore

RUN pip install /tmp/*.whl && rm -rf /tmp/*.whl

CMD ["uvicorn", "gpdp.server:app", "--host", "0.0.0.0", "--port", "8000"]
