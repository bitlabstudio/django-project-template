"""Tests for the context processors of the ``var_project_name`` project."""
from django.test import TestCase

from .. import context_processors


class ProjectSettingsTestCase(TestCase):
    longMessage = True

    def test_processors(self):
        self.assertTrue(
            context_processors.project_settings({}).get('LIVERELOAD'))
