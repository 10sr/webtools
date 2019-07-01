WEBTOOLS_PORT ?= 7700
# 0.0.0.0 is required when run inside of docker container
WEBTOOLS_HOST ?= 0.0.0.0

REDIS_PORT ?= 7799

pipenv := pipenv
python3 := $(pipenv) run python3

# Meta targets ##############

start: gunicorn

check: app-test check-format check-type

check-format: flake8

check-type: mypy


# Initialize ##################

installdeps: semanticui
	$(pipenv) install --deploy

installdeps-dev:
	$(pipenv) install --dev --deploy


SEMANTIC_UI_VERSION := 2.4.1
# semantic-ui
semanticui: Semantic-UI-CSS-$(SEMANTIC_UI_VERSION).tar.gz
	tar -vxf $^
	rm -rfv static/semanticui/
	mkdir -p static
	cp -rv Semantic-UI-CSS-$(SEMANTIC_UI_VERSION)/ static/semanticui/

# https://github.com/Semantic-Org/Semantic-UI-CSS
Semantic-UI-CSS-$(SEMANTIC_UI_VERSION).tar.gz:
	wget https://github.com/Semantic-Org/Semantic-UI-CSS/archive/$(SEMANTIC_UI_VERSION).tar.gz \
		-O $@

# Tests ##################

app-test:
	WEBTOOLS_SETTINGS_TOML=tests/settings_deploy_example.toml $(python3) manage.py check --deploy --fail-level WARNING
	WEBTOOLS_SETTINGS_TOML=tests/settings.toml $(python3) manage.py makemigrations --dry-run --check
	WEBTOOLS_SETTINGS_TOML=tests/settings.toml $(pipenv) run coverage run ./manage.py test tests/ --pattern='*.py'

codecov:
	$(pipenv) run codecov


# Run ###################333

runserver:
	$(python3) manage.py runserver "$(WEBTOOLS_HOST):$(WEBTOOLS_PORT)"

# gunicorn cannot serve static files in debug mode
gunicorn:
	$(pipenv) run gunicorn \
		--bind "$(WEBTOOLS_HOST):$(WEBTOOLS_PORT)" \
		--workers 2 \
		--capture-output \
		--enable-stdio-inheritance \
		--access-logfile - \
		--reload \
		webtools.wsgi:application

startapp:
	$(python3) manage.py $@ $(app) $(directory)

migrate collectstatic:
	$(python3) manage.py $@


get_random_secret_key:
	$(python3) -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Honcho ################

# honcho_target: Space separated honcho targets, left blank to run all
honcho:
	$(pipenv) run honcho start $(honcho_target)


# Targets for honcho #######################

proc-web: runserver

proc-redis:
	redis-server --port $(REDIS_PORT)


# Docker ###################

docker-build:
	docker build . -t local/webtools

docker-run: docker-stop
	docker run \
		--name webtools01 \
		--rm \
		-p '$(TRIGGER_PORT):$(TRIGGER_PORT)' \
		--env-file env.secret \
		local/webtools

docker-stop:
	docker stop webtools01 || true



# Formatter and Linter ###############

flake8:
	$(pipenv) run flake8 --version
	$(pipenv) run flake8 .

# black

black:
	$(pipenv) run black .

# isort

isort:
	$(pipenv) run isort -rc .

# mypy ########################

mypy:
	$(pipenv) run mypy .
