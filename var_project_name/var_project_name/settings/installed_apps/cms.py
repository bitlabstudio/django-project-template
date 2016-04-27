"""Settings for the ``cms`` app."""
from django.utils.translation import ugettext_lazy as _


CMS_TEMPLATES = (
    ('cms/cms.html', _('Standard')),
    ('cms/cms_contact_form.html', _('Contact Form')),
)
TEXT_SAVE_IMAGE_FUNCTION = \
    'cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'
CMS_TOOLBAR_ANONYMOUS_ON = False
