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
    'admin_honeypot',
    'debug_toolbar',
    'django_libs',
    'honeypot_signals',
    'mailer',
    'south',
]

INTERNAL_APPS = [
    'VAR_PROJECT_NAME',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS
