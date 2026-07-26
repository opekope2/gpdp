FROM python:alpine AS builder

WORKDIR /build

COPY . .

ENV PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_ROOT_USER_ACTION=ignore

RUN pip install build && python -m build --wheel

FROM python:alpine

WORKDIR /app

COPY --from=builder /build/logging.json /app/

COPY --from=builder /build/dist/*.whl /tmp/

ENV PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_ROOT_USER_ACTION=ignore

RUN pip install /tmp/*.whl && rm -rf /tmp/*.whl && adduser -s /sbin/nologin -D gpdp

USER gpdp

EXPOSE 8000

CMD ["uvicorn", "gpdp.server:app", "--host", "0.0.0.0"]
