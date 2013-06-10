"""Installed apps for the VAR_PROJECT_NAME project."""
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
    'south',
    'django_libs',
    'debug_toolbar',
    'mailer',
]

INTERNAL_APPS = [
    'VAR_PROJECT_NAME',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS
