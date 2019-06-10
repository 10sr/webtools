WEBTOOLS_PORT ?= 7700
# 0.0.0.0 is required when run inside of docker container
WEBTOOLS_HOST ?= 0.0.0.0

REDIS_PORT ?= 7799

pipenv := pipenv
python3 := $(pipenv) run python3


installdeps:
	$(pipenv) install --deploy

start: gunicorn


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

check-format: black-check isort-check pydocstyle

# black

black:
	$(pipenv) run black .

black-check:
	$(pipenv) run black --check .

# isort
isort_target_dirs := webtools lggr export_as_bookmark

isort:
	$(pipenv) run isort -rc $(isort_target_dirs)

isort-check:
	$(pipenv) run isort -rc $(isort_target_dirs) -c -vb

# pydocstyle

pydocstyle:
	$(pipenv) run pydocstyle .
