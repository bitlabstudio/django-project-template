# flake8: noqa
import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "var_project_name.settings")

from development_fabfile.fabfile import *
