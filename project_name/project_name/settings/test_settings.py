# flake8: noqa
"""Settings to be used for running tests."""
from ..settings import *


INSTALLED_APPS.append('django_nose')


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}


PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


EMAIL_SUBJECT_PREFIX = '[test VAR_PROJECT_NAME] '
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
SOUTH_TESTS_MIGRATE = False


TEST_RUNNER = 'django_libs.testrunner.NoseCoverageTestRunner'
COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'settings$', 'urls$', 'locale$', 'wsgi$', 'testrunner$',
    'migrations', 'fixtures', 'admin$', 'django_extensions',
]
COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS
COVERAGE_MODULE_EXCLUDES += DJANGO_APPS
COVERAGE_REPORT_HTML_OUTPUT_DIR = "coverage"
