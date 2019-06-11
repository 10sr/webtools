[![Build Status](https://travis-ci.org/10sr/webtools.svg?branch=master)](https://travis-ci.org/10sr/webtools)
[![codecov](https://codecov.io/gh/10sr/webtools/branch/master/graph/badge.svg)](https://codecov.io/gh/10sr/webtools)


webtools
========

Small Web Tools (No Need to Login)


Requirements
------------

- Python3
- Pipenv
- Redis


Run Server
----------

First, copy `settings_local.toml` to `settings.toml` and edit that file.

    make installdeps
    make honcho
