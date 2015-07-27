"""Installed apps for the ``var_project_name`` project."""
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangocms_admin_style',  # Needs to be added before 'django.contrib.admin'
    'django.contrib.admin',
]

EXTERNAL_APPS = [
    # allauth apps. Choose your favourites.
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.amazon',
    # 'allauth.socialaccount.providers.angellist',
    # 'allauth.socialaccount.providers.bitbucket',
    # 'allauth.socialaccount.providers.bitly',
    # 'allauth.socialaccount.providers.dropbox',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.flickr',
    # 'allauth.socialaccount.providers.feedly',
    # 'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.linkedin_oauth2',
    # 'allauth.socialaccount.providers.openid',
    # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.soundcloud',
    # 'allauth.socialaccount.providers.stackexchange',
    # 'allauth.socialaccount.providers.tumblr',
    # 'allauth.socialaccount.providers.twitch',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.vimeo',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.weibo',

    # django-cms apps
    # 'djangocms_file',
    # 'djangocms_flash',
    # 'djangocms_googlemap',
    # 'djangocms_inherit',
    # 'djangocms_picture',
    # 'djangocms_teaser',
    # 'djangocms_video',
    # 'djangocms_link',
    # 'djangocms_snippet',
    'djangocms_text_ckeditor',
    'cms',
    'mptt',
    'menus',
    'sekizai',
    'treebeard',

    # django-filer apps
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    'admin_honeypot',
    'compressor',
    'contact_form',
    'debug_toolbar',
    'django_extensions',
    'django_libs',
    'feedback_form',
    'generic_positions',
    'honeypot_signals',
    'mailer',
    'user_media',
]

INTERNAL_APPS = [
    'var_project_name',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS

from .allauth import *  # NOQA
from .cms import *  # NOQA
from .compressor import *  # NOQA
from .contact_form import *  # NOQA
from .debug_toolbar import *  # NOQA
from .easy_thumbnails import *  # NOQA
from .user_media import *  # NOQA
