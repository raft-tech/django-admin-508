# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ARG user=tdpuser
ARG group=tdpuser
ARG uid=1000
ARG gid=1000
ENV DJANGO_CONFIGURATION=Local

COPY . /code/
WORKDIR /code/

RUN groupadd -g ${gid} ${group} && useradd -u ${uid} -g ${group} -s /bin/sh ${user}

RUN pip install -r requirements.txt
