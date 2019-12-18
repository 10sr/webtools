[![Build Status](https://travis-ci.org/10sr/webtools.svg?branch=master)](https://travis-ci.org/10sr/webtools)
[![codecov](https://codecov.io/gh/10sr/webtools/branch/master/graph/badge.svg)](https://codecov.io/gh/10sr/webtools)
[![Docker Repository on Quay](https://quay.io/repository/10sr/webtools/status "Docker Repository on Quay")](https://quay.io/repository/10sr/webtools)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)


webtools
========

Small Web Tools (Without Login)


Requirements
------------

- Python3 >= 3.7
- Pipenv
- Redis


Run Server
----------

First, copy `settings_insecure.toml` to `settings.toml` and edit that file.

    make installdeps
    make honcho
