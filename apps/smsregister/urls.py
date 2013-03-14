"""
URLs for app smsregister
"""

from django.conf.urls.defaults import patterns, url

from .views import Show, Thanks



urlpatterns = patterns('',
    url(r'^$', Show.as_view(), name='smsregister_show'),
    url(r'^thanks/$', Thanks.as_view(), name='smsregister_thanks'),
)
