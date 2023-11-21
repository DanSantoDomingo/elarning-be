FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN apt-get update
RUN python3 -m pip install --upgrade pip
RUN pip3 install poetry && poetry config virtualenvs.create false && poetry install --no-dev

COPY . /app/
RUN chmod +x docker/entrypoint.sh
RUN chmod +x docker/start_django.sh

ENTRYPOINT ["/app/docker/entrypoint.sh"]
