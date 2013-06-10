# flake8: noqa
from VAR_PROJECT_NAME import settings
from django.core.management import setup_environ
setup_environ(settings)

from development_fabfile.fabfile import *
