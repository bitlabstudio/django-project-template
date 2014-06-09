"""Settings for the project's fabfile."""
import os

from fabric.api import env

# ============================================================================
# General settings
# ============================================================================

# This should be the folder name of your Django project
PROJECT_NAME = 'var_project_name'

# Path to your test_settings.py
TEST_SETTINGS_PATH = 'var_project_name.settings.test_settings'

# This should be the name of the virtualenv on your local machine and on your
# servers
VENV_NAME = PROJECT_NAME

# You should keep db role and db name identical on your local machine and on
# your servers
DB_ROLE = PROJECT_NAME
DB_NAME = PROJECT_NAME
DB_DUMP_FILENAME = '{0}.dump'.format(PROJECT_NAME)
MEDIA_DUMP_FILENAME = '{0}_media.tar.gz'.format(PROJECT_NAME)

# Set this to true if you want to execute makemessages during a deployment
MAKEMESSAGES_ON_DEPLOYMENT = False

# Set this to true if you want to execute compilemessages during a deployment
COMPILEMESSAGES_ON_DEPLOYMENT = False

# Add other code snippets you want to be found. Add a file type to the dict and
# define a regex, which should be processed
SYNTAX_CHECK = {
    '*.js': '(console.log|alert)',
}
# Add files or directories to exclude in the syntax check
SYNTAX_CHECK_EXCLUDES = [
    './submodules',
    'static/js/libs/',
]


# ============================================================================
# Local settings
# ============================================================================

# This should be the superuser of your postgres installation. Usually this is
# either postgres or your login username.
LOCAL_PG_ADMIN_ROLE = 'postgres'
LOCAL_PG_USE_LOCALHOST = True
LOCAL_COVERAGE_PATH = os.path.join(os.path.dirname(__file__), '../../coverage')

# ============================================================================
# Server settings
# ============================================================================

# This should be the name of your user that has sudo access on the server
LOGIN_USER_DEV = '{0}3'.format(PROJECT_NAME)
LOGIN_USER_STAGE = '{0}2'.format(PROJECT_NAME)
LOGIN_USER_PROD = PROJECT_NAME
HOST_DEV = None
HOST_STAGE = None
HOST_PROD = '{0}.webfactional.com'.format(LOGIN_USER_PROD)

RSYNC_EXCLUDES = [
    'local_settings.py',
    'circus.ini',
]


# These are some paths that, by convention, you set on your servers.
# You should keep them identical for all tiers (dev, stage, prod).
def get_fab_setting(setting_name):
    if setting_name == 'SERVER_APACHE_BIN_DIR':
        return '/home/{0}/webapps/{1}_django/apache2/bin/'.format(
            env.user, PROJECT_NAME)
    if setting_name == 'SERVER_REPO_ROOT':
        return '/home/{0}/src/{1}/'.format(env.user, PROJECT_NAME)

    if setting_name == 'SERVER_REPO_PROJECT_ROOT':
        # This must have no trailing slash because of rsync
        return '{0}{1}'.format(
            get_fab_setting('SERVER_REPO_ROOT'), PROJECT_NAME)

    if setting_name == 'SERVER_APP_ROOT':
        return '/home/{0}/webapps/{1}_django/'.format(
            env.user, PROJECT_NAME)

    if setting_name == 'SERVER_PROJECT_ROOT':
        return '{0}{1}/'.format(
            get_fab_setting('SERVER_APP_ROOT'), PROJECT_NAME)

    if setting_name == 'SERVER_REQUIREMENTS_PATH':
        return '{0}/requirements.txt'.format(
            get_fab_setting('SERVER_REPO_PROJECT_ROOT'))

    if setting_name == 'SERVER_MEDIA_ROOT':
        return '/home/{0}/webapps/{1}_media/'.format(
            env.user, PROJECT_NAME)

    if setting_name == 'SERVER_DB_BACKUP_DIR':
        return '/home/{0}/backups/{1}/postgres/'.format(
            env.user, PROJECT_NAME)

    if setting_name == 'SERVER_MEDIA_BACKUP_DIR':
        return '/home/{0}/backups/{1}/media/'.format(
            env.user, PROJECT_NAME)

    if setting_name == 'SERVER_WSGI_FILE':
        return '{0}{1}/wsgi.py'.format(
            get_fab_setting('SERVER_PROJECT_ROOT'), PROJECT_NAME)


FAB_SETTING = lambda x: get_fab_setting(x)
