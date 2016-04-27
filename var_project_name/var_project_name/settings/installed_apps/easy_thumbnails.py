"""Settings for the ``easy_thumbnails`` app."""
THUMBNAIL_BASEDIR = 'thumbs'
THUMBNAIL_CACHE_DIMENSIONS = True
THUMBNAIL_PROCESSORS = (
    # 'user_media.processors.crop_box',
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
