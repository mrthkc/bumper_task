import os

from django.core.exceptions import ImproperlyConfigured


def get_env_value(env_variable):
    try:
        return os.environ[env_variable]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(env_variable)
        raise ImproperlyConfigured(error_msg)


ENV = "development"
try:
    ENV = get_env_value("ENVIRONMENT")
except ImproperlyConfigured:
    print("Environment stays as {}".format(ENV))

SECRET_KEY = get_env_value("SECRET_KEY")
DB_HOST = get_env_value("DB_HOST")
DB_NAME = get_env_value("DB_NAME")
DB_USER = get_env_value("DB_USER")
DB_PASSWORD = get_env_value("DB_PASSWORD")
