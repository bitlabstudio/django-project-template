# flake8: noqa
import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "VAR_PROJECT_NAME.settings")

from development_fabfile.fabfile import *
