"""Views for the var_project_name project."""
from allauth.account.views import LoginView

from django_libs.views_mixins import AjaxResponseMixin


class AJAXnonAJAXLoginView(AjaxResponseMixin, LoginView):
    pass
