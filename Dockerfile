FROM python:3

# Name PIPENV_VERSION is used by pipenv itself
ENV PIPENV_VERSION_ 2018.11.26

ENV WEBTOOLS_PORT 7700

# envsubst: For templating settings.toml
# TODO: Remove cache
RUN apt update && apt install -y gettext

WORKDIR /root/app

RUN pip3 install pipenv==$PIPENV_VERSION_

COPY Pipfile Pipfile.lock ./
RUN env -u PIPENV_VERSION pipenv install --deploy # --system

COPY webtools ./
COPY export_as_bookmark ./
COPY Makefile manage.py ./

EXPOSE $WEBTOOLS_PORT

# TODO: Pass via build argument
#RUN git rev-parse HEAD >git_commit_hash.txt

# Django not work without this!
ENV PYTHONUNBUFFERED 1
CMD ["make", "migrate", "gunicorn"]
