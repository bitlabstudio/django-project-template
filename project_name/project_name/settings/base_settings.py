"""Settings that can be imported by the other settings files."""
import os


# The folder where your manage.py file is
DJANGO_PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..'))
