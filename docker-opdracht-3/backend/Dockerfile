FROM alpine:3.19

RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-virtualenv \
    build-base \
    libffi-dev \
    openssl-dev \
    ca-certificates

RUN adduser -D appuser


WORKDIR /app

COPY . .


RUN python3 -m venv /app/venv && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

RUN /app/venv/bin/pip install pytest


RUN /app/venv/bin/pytest -v /app/tests/test_app.py

USER appuser

ENV PATH="/app/venv/bin:$PATH"

CMD ["python", "app.py"]