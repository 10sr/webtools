WEBTOOLS_PORT ?= 7700
# 0.0.0.0 is required when run inside of docker container
WEBTOOLS_HOST ?= 0.0.0.0

REDIS_PORT ?= 7799

pipenv := pipenv
python3 := $(pipenv) run python3

# Meta targets ##############

start: gunicorn

check: app-test check-format check-type check-docstrings

check-format: flake8 black-check isort-check

check-type: mypy

check-docstrings: pydocstyle darglint


# Initialize ##################

installdeps:
	$(pipenv) install --deploy

installdeps-dev:
	$(pipenv) install --dev --deploy


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

migrate:
	$(python3) manage.py $@


get_random_secret_key:
	$(python3) -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Honcho ################

honcho:
	REDIS_PORT=$(REDIS_PORT) $(pipenv) run honcho start


# Targets for honcho #######################

proc-web: gunicorn

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
	$(pipenv) run flake8 .

# black

black:
	$(pipenv) run black .

black-check:
	$(pipenv) run black --check .

# isort

isort:
	$(pipenv) run isort -rc .

isort-check:
	$(pipenv) run isort -rc . -c

# mypy ########################

mypy:
	$(pipenv) run mypy .


# docstring ####################

# pydocstyle

pydocstyle:
	$(pipenv) run pydocstyle .

# darglint

darglint:
	# Is git always available?
	git ls-files '*.py' | grep -v ^tests/ | \
		xargs pipenv run darglint -v 2 -m '{path}:{line}:{obj} ({msg_id}) {msg}'
