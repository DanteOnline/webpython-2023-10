from .base_settings import *  # pylint: disable=wildcard-import, unused-wildcard-import

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
