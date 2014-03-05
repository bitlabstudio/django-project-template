"""Settings for the ``compressor`` app."""
from ...settings import local_settings

COMPRESS_ENABLED = getattr(local_settings, 'LOCAL_COMPRESS_ENABLED', True)
