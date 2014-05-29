"""Installed apps for the ``var_project_name`` project."""
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

EXTERNAL_APPS = [
    'admin_honeypot',
    'compressor',
    'debug_toolbar',
    'django_libs',
    'honeypot_signals',
    'mailer',
    'south',
    'rapid_prototyping',
]

INTERNAL_APPS = [
    'var_project_name',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS

from .compressor import *  # NOQA
from .rapid_prototyping import *  # NOQA
from .debug_toolbar import *  # NOQA
