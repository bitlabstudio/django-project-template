# flake8: noqa
from .django_settings import *
from .installed_apps import *
from .fabfile_settings import *
from .local_settings import *

# This enabled you to have a ``DISABLED_APPS = ['foorbar', ]`` setting in your
# local settings to easily disable apps that otherwise have a complex setup
# throughout various different other settings.
if 'DISABLED_APPS' in locals():
    INSTALLED_APPS = list(INSTALLED_APPS)
    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS)

    for app in DISABLED_APPS:
        for index, app_name in enumerate(INSTALLED_APPS):
            if app_name.startswith(app):
                INSTALLED_APPS.pop(index)

        for index, app_name in enumerate(MIDDLEWARE_CLASSES):
            if app_name.startswith(app):
                MIDDLEWARE_CLASSES.pop(index)

        for index, app_name in enumerate(TEMPLATE_CONTEXT_PROCESSORS):
            if app_name.startswith(app):
                TEMPLATE_CONTEXT_PROCESSORS.pop(index)
