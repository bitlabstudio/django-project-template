"""Settings for the ``contact_form`` app."""
try:
    from ..local_settings import MANAGERS
except ImportError:
    MANAGERS = []

CONTACT_FORM_RECIPIENTS = MANAGERS
