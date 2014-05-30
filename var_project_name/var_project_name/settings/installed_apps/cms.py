"""Settings for the ``cms`` app."""
CMS_TEMPLATES = (
    ('cms/cms.html', 'Standard'),
    ('cms/cms_contact_form.html', 'Contact Form'),
)
TEXT_SAVE_IMAGE_FUNCTION = \
    'cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'
