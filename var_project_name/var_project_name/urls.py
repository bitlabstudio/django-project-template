"""URLs for the var_project_name project."""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

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
    urlpatterns += patterns(
        '',
        (r'^404/$', 'django.views.defaults.page_not_found'),
        (r'^500/$', 'django.views.defaults.server_error'),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

urlpatterns += patterns(
    '',
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
        'sitemaps': {
            'cms': CMSSitemap,
        },
    }),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {}),
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^admin-.+/', include('admin_honeypot.urls')),
    url(r'^accounts/login/$', AJAXnonAJAXLoginView.as_view(),
        name='account_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
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
