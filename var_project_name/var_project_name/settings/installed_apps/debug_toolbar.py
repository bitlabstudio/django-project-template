"""Settings for the ``debug_toolbar`` app."""
DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': 'var_project_name.settings.installed_apps.debug_toolbar.show_toolbar',  # NOQA
}


def show_toolbar(request):
    return True


def hide_toolbar(request):
    return False
