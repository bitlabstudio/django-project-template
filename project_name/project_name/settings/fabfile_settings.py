"""Settings for the project's fabfile."""
import os

# ============================================================================
# General settings
# ============================================================================

# This should be the folder name of your Django project
PROJECT_NAME = 'VAR_PROJECT_NAME'

# This should be the name of the virtualenv on your local machine and on your
# servers
VENV_NAME = PROJECT_NAME

# You should keep db role and db name identical on your local machine and on
# your servers
DB_ROLE = PROJECT_NAME
DB_NAME = PROJECT_NAME
DB_DUMP_FILENAME = '{0}.dump'.format(PROJECT_NAME)


# ============================================================================
# Local settings
# ============================================================================

# This should be the superuser of your postgres installation. Usually this is
# either postgres or your login username.
LOCAL_PG_ADMIN_ROLE = 'postgres'
LOCAL_COVERAGE_PATH = os.path.join(os.path.dirname(__file__), '../../coverage')

# ============================================================================
# Server settings
# ============================================================================

# This should be the name of your user that has sudo access on the server
LOGIN_USER = PROJECT_NAME
HOST_DEV = None
HOST_STAGE = None
HOST_PROD = '{0}.webfactional.com'.format(LOGIN_USER)

RSYNC_EXCLUDES = [
    'local_settings.py',
]

# These are some paths that, by convention, you set on your servers.
# You should keep them identical for all tiers (dev, stage, prod).
SERVER_APACHE_BIN_DIR = '/home/{0}/webapps/{1}_django/apache2/bin/'.format(
            LOGIN_USER, PROJECT_NAME)
SERVER_REPO_ROOT = '/home/{0}/src/{1}/'.format(LOGIN_USER, PROJECT_NAME)

# This must have no trailing slash because of rsync
SERVER_REPO_PROJECT_ROOT = '{0}{1}'.format(SERVER_REPO_ROOT, PROJECT_NAME)
SERVER_APP_ROOT = '/home/{0}/webapps/{1}_django/'.format(
            LOGIN_USER, PROJECT_NAME)

SERVER_PROJECT_ROOT = '{0}{1}/'.format(SERVER_APP_ROOT, PROJECT_NAME)
SERVER_REQUIREMENTS_PATH = '{0}/requirements.txt'.format(
            SERVER_REPO_PROJECT_ROOT)

SERVER_MEDIA_ROOT = '/home/{0}/webapps/{1}_media/'.format(
            LOGIN_USER, PROJECT_NAME)
SERVER_DB_BACKUP_DIR = '/home/{0}/backups/{1}/postgres/'.format(LOGIN_USER,
            PROJECT_NAME)
SERVER_MEDIA_BACKUP_DIR = '/home/{0}/backups/media/'.format(LOGIN_USER)
SERVER_WSGI_FILE = '{0}{1}/wsgi.py'.format(
            SERVER_PROJECT_ROOT, PROJECT_NAME)
