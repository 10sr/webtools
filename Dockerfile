FROM python:3.8

# Name PIPENV_VERSION is used by pipenv itself
ENV PIPENV_VERSION_ 2018.11.26

ENV WEBTOOLS_PORT 7700

# envsubst: For templating settings.toml
# TODO: Remove cache
RUN apt update && apt install -y gettext

WORKDIR /root/app

RUN pip3 install pipenv==$PIPENV_VERSION_

COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy # --system
COPY download_semanticui.sh ./
RUN bash ./download_semanticui.sh

COPY webtools webtools
COPY lggr lggr
COPY export_as_bookmark export_as_bookmark
COPY Makefile manage.py settings_insecure.toml ./

COPY .git/HEAD .git/
COPY .git/refs .git/refs
RUN mkdir -p .git/objects && git rev-parse HEAD >HEAD.txt && cat HEAD.txt

EXPOSE $WEBTOOLS_PORT

# Django not work without this!
ENV PYTHONUNBUFFERED 1
CMD ["make", "migrate", "collectstatic", "gunicorn"]
