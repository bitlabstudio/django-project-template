"""URLs for the VAR_PROJECT_NAME project."""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

from django_libs.views import RapidPrototypingView


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

urlpatterns += patterns(
    '',
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^admin-.+/', include('admin_honeypot.urls')),
    url(r'^p/', include('rapid_prototyping.urls')),
    url(r'^p/(?P<template_path>.*)$',
        RapidPrototypingView.as_view(),
        name='prototype'),
    url(r'^$', RedirectView.as_view(url='/p/proto/home.html')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
