"""Tests for the views of the ``var_project_name`` project."""
from django.test import TestCase

from django_libs.tests.views_tests import ViewRequestFactoryTestMixin

from .. import views


class AJAXnonAJAXLoginViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    view_class = views.AJAXnonAJAXLoginView

    def test_view(self):
        self.is_callable()
