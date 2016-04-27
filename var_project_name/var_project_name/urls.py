"""URLs for the var_project_name project."""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.sitemaps import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.cache import cache_page
from django.views.defaults import page_not_found, server_error
from django.views.generic import TemplateView
from django.views.i18n import javascript_catalog
from django.views.static import serve

from cms.sitemaps import CMSSitemap
from django_libs.views import UpdateSessionAJAXView

from .views import AJAXnonAJAXLoginView


LOGOUT_REDIRECT_URL = getattr(settings, 'ACCOUNT_LOGOUT_REDIRECT_URL', '/')

admin.autodiscover()

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG is False and settings.SANDBOX is True:
    # If you want to set DEBUG=False on your local machine, Django would no
    # longer serve static files and you would have to setup Apache or Nginx.
    # This hack allows Django to serve staticfiles (which is slow and insecure)
    urlpatterns += i18n_patterns(
        url(r'^404/$', page_not_found),
        url(r'^500/$', server_error),
        url(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += i18n_patterns(
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

sitemaps = {
    'cmspages': CMSSitemap,
}


@cache_page(60 * 60 * 4)
def cached_javascript_catalog(request, domain='djangojs', packages={
        'packages': ('var_project_name', )}):
    return javascript_catalog(request, domain, packages)

urlpatterns += i18n_patterns(
    url(r'^sitemap\.xml$', views.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap, {
        'sitemaps': sitemaps}),
    url(r'^jsi18n.js$', cached_javascript_catalog, name='javascript_catalog'),
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^admin-.+/', include('admin_honeypot.urls')),
    url(r'^accounts/login/$', AJAXnonAJAXLoginView.as_view(),
        name='account_login'),
    url(r'^accounts/logout/$', logout,
        {'next_page': LOGOUT_REDIRECT_URL}, name='account_logout'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^pos/', include('generic_positions.urls')),
    url(r'^umedia/', include('user_media.urls')),
    url(r'^feedback/', include('feedback_form.urls')),
    url(r'^cms/', include('cms.urls')),
    url(r'^update-session/$', UpdateSessionAJAXView.as_view(),
        name='update_session'),
    url(r'^$', TemplateView.as_view(template_name='base.html')),
)
