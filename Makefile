WEBTOOLS_PORT ?= 7700
# 0.0.0.0 is required when run inside of docker container
WEBTOOLS_HOST ?= 0.0.0.0

REDIS_PORT ?= 7799

pipenv := pipenv
python3 := $(pipenv) run python3


runserver-viamanager:
	$(python3) manage.py runserver "$(WEBTOOLS_HOST):$(WEBTOOLS_PORT)"

runserver:
	$(pipenv) run gunicorn \
		--bind "$(WEBTOOLS_HOST):$(WEBTOOLS_PORT)" \
		--workers 2 \
		--capture-output \
		--enable-stdio-inheritance \
		--access-logfile - \
		--reload \
		webtools.wsgi:application

startapp:
	$(python3) manage.py $@ $(app)



# Honcho ################

honcho:
	REDIS_PORT=$(REDIS_PORT) $(pipenv) run honcho start


# Targets for honcho #######################

honcho-web: runserver

honcho-redis:
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
		local/trigger

docker-stop:
	docker stop webtools01 || true
