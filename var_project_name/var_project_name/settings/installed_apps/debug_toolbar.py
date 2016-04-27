"""Settings for the debug_toolbar app."""
from django.conf import settings


def show_toolbar(request):
    return settings.DEBUG


DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    'INTERCEPT_REDIRECTS': False,
}
