"""
Django settings for webtools project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from typing import Optional

import dj_database_url

from .config import Config

_c = Config.from_toml(
    os.environ.get("WEBTOOLS_SETTINGS_TOML", "settings.toml"), "webtools"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _c.DEBUG

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

SECRET_KEY = _c.SECRET_KEY

ALLOWED_HOSTS = [_c.ALLOWED_HOST]
USE_X_FORWARDED_HOST = _c.USE_X_FORWARDED_HOST

# Security configurations

SECURE_HSTS_SECONDS = _c.SECURE_HSTS_SECONDS
SECURE_HSTS_INCLUDE_SUBDOMAINS = _c.SECURE_HSTS_INCLUDE_SUBDOMAINS
SECURE_HSTS_PRELOAD = _c.SECURE_HSTS_PRELOAD

SECURE_CONTENT_TYPE_NOSNIFF = _c.SECURE_CONTENT_TYPE_NOSNIFF
SECURE_BROWSER_XSS_FILTER = _c.SECURE_BROWSER_XSS_FILTER
SECURE_SSL_REDIRECT = _c.SECURE_SSL_REDIRECT
SESSION_COOKIE_SECURE = _c.SESSION_COOKIE_SECURE
CSRF_COOKIE_SECURE = _c.CSRF_COOKIE_SECURE
X_FRAME_OPTIONS = _c.X_FRAME_OPTIONS

# Application definition

INSTALLED_APPS = [
    # Do not forget to add app or django cannot find templates!
    "webtools.rootapp.apps.RootappConfig",
    "export_as_bookmark.apps.ExportAsBookmarkConfig",
    "lggr.apps.LggrConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "webtools.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "webtools.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {"default": dj_database_url.parse(_c.DATABASE_URL)}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"


# webtools specific

WEBTOOLS_REVISION_FILEPATH = _c.WEBTOOLS_REVISION_FILEPATH
WEBTOOLS_REVISION: Optional[str] = None
try:
    if WEBTOOLS_REVISION_FILEPATH is not None:
        with open(WEBTOOLS_REVISION_FILEPATH) as f:
            WEBTOOLS_REVISION = f.read().strip()
except FileNotFoundError:
    # TODO: Remove try?
    pass


# Use Redis.from_url
EXPORT_AS_BOOKMARK_REDIS_URL = _c.EXPORT_AS_BOOKMARK_REDIS_URL
