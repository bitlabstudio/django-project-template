"""Context processors for the var_project_name project."""
from django.conf import settings


def project_settings(request):
    "A context processor that adds important settings to the context."
    return {
        'LIVERELOAD': getattr(settings, 'LIVERELOAD', False),
    }
