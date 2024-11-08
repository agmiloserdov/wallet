FROM python:3.11-slim as base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWIRTEBYTECODE=1
ENV PYSETUP_PATH=/opt/pysetup
ENV VENV_PATH=$PYSETUP_PATH/.venv
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VERSION=1.3.1
ENV POETRY_HOME=/opt/poetry/
ENV PATH=$POETRY_HOME/bin:$PATH

WORKDIR $PYSETUP_PATH

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    libssl-dev \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install poetry

FROM base AS builder

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install -n

ARG STATIC_ROOT
ENV STATIC_ROOT=${STATIC_ROOT:-/static/}

ARG MEDIA_ROOT
ENV MEDIA_ROOT=${MEDIA_ROOT:-/media/}

ARG PORT
ENV PORT=${PORT:-8080}

ARG PROCESSES_NUM
ENV PROCESSES_NUM=${PROCESSES_NUM:-4}

WORKDIR /app
COPY . /app

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "code.config.server.wsgi:application"]