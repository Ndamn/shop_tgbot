FROM python:3.8

WORKDIR /src
COPY poetry.lock pyproject.toml /src/

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir poetry \
 && poetry install --no-dev
 

COPY . /src