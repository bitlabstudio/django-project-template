# flake8: noqa
"""Settings to be used for running tests."""
import logging

from ..settings import *


INSTALLED_APPS.append('django_nose')


logging.getLogger("factory").setLevel(logging.WARN)


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}


PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


EMAIL_SUBJECT_PREFIX = '[test var_project_name] '
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'


class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"

MIGRATION_MODULES = DisableMigrations()
