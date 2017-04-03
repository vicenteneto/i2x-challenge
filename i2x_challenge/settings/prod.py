"""Production settings and globals."""

from __future__ import absolute_import

from os import environ

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

from .base import *


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


# DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'i2x_challenge',
        'HOST': get_env_setting('I2X_DATABASE_HOST'),
        'PORT': get_env_setting('I2X_DATABASE_PORT'),
        'USER': get_env_setting('I2X_DATABASE_USER'),
        'PASSWORD': get_env_setting('I2X_DATABASE_PASSWORD')
    }
}
# END DATABASE CONFIGURATION


# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('I2X_SECRET_KEY')
# END SECRET CONFIGURATION
