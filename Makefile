WEBTOOLS_PORT ?= 7700
# 0.0.0.0 is required when run inside of docker container
WEBTOOLS_HOST ?= 0.0.0.0

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
