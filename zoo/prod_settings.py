from os import getenv
from .base_settings import *  # pylint: disable=wildcard-import, unused-wildcard-import

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getenv('PGDB'),
        "USER": getenv('PGUSER'),
        "PASSWORD": getenv('PGPASSWORD'),
        "HOST": "db",
        "PORT": "5432",
    }
}

ALLOWED_HOSTS = ['127.0.0.1', '127.0.0.1:8000', 'localhost', 'localhost:8000']
