from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('website.views',
    url(r'^$', 'index'),
    url(r'(?i)drbetty$', 'drbetty'),
    url(r'(?i)health$', 'health'),
    url(r'(?i)sports$', 'sports'),
    url(r'(?i)lifecoach$', 'lifecoach'),
    url(r'(?i)downloads$', 'downloads'),
)
