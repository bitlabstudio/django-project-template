"""Django settings for the ``var_project_name`` project."""
import os

from django.contrib import messages

from django_libs.settings.django_settings import IGNORABLE_404_URLS as LIBS_IGNORABLE_404_URLS  # NOQA
from django_libs.settings.django_settings import IGNORABLE_404_USER_AGENTS  # NOQA

from .base_settings import DJANGO_PROJECT_ROOT
from .local_settings import DEBUG


IGNORABLE_404_URLS = LIBS_IGNORABLE_404_URLS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
]

LOCALE_PATHS = (
    os.path.join(DJANGO_PROJECT_ROOT, 'locale'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DJANGO_PROJECT_ROOT, 'var_project_name/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django_libs.middleware.AjaxRedirectMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(DJANGO_PROJECT_ROOT, 'var_project_name/templates')],
    'OPTIONS': {
        'debug': DEBUG,
        'loaders': (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
            'django.template.loaders.eggs.Loader',
        ),
        'context_processors': (
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.i18n',
            'django.template.context_processors.request',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.contrib.messages.context_processors.messages',
            'django_libs.context_processors.analytics',
            'sekizai.context_processors.sekizai',
            'cms.context_processors.cms_settings',
            'var_project_name.context_processors.project_settings',
        )
    }
}]

MIGRATION_MODULES = {
    # Remove these modules, after installing cmsplugin-filer>=1.1
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
}

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-error',
}

ROOT_URLCONF = 'var_project_name.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'var_project_name.wsgi.application'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'filter_ignorable_404_urls': {
            '()': 'django_libs.utils_log.FilterIgnorable404URLs'
        },
        'add_current_user': {
            '()': 'django_libs.utils_log.AddCurrentUser'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'WARNING',
            'filters': [
                'require_debug_false',
                'filter_ignorable_404_urls',
                'add_current_user',
            ],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(DJANGO_PROJECT_ROOT, 'debugger.log'),
            'maxBytes': 16777216,  # 16megabytes
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'WARNING',
            'propagate': True,
        },

        # For emergency logging on the server, add this into your code to
        # generate log output in debugger.log:
        #
        # import logging
        # logger = logging.getLogger('debugger')
        # logger.debug('Some debug output')
        #
        'debugger': {
            'handlers': ['log_file', ],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
