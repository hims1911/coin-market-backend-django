FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
# RUN apt-get update && \
#     apt-get install -y libpq-dev gcc && \
#     rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt
ENV DJANGO_SETTINGS_MODULE=backend.settings

COPY . /code/