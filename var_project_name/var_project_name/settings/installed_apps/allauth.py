"""Settings for the ``allauth`` app."""
from ..local_settings import DEFAULT_HTTP_PROTOCOL


AUTH_USER_MODEL = 'auth.User'
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/'

# Allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
ACCOUNT_DEFAULT_HTTP_PROTOCOL = DEFAULT_HTTP_PROTOCOL
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'
ACCOUNT_USER_DISPLAY = \
    'var_project_name.settings.installed_apps.allauth.get_username'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_PASSWORD_MIN_LENGTH = 7
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'public_profile', 'user_friends', 'user_location'],
    },
    'google': {
        'SCOPE': ['email', 'profile',
                  'https://www.googleapis.com/auth/contacts.readonly', ],
    },
}


def get_username(user):
    """Standard return of an ``allauth`` username."""
    return user.email
