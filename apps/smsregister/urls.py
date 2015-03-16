"""
URLs for app smsregister
"""

from django.conf.urls.defaults import patterns, url

from .views import Show, Thanks, Unsubscribe



urlpatterns = patterns('',
    url(r'^$', Show.as_view(), name='smsregister_show'),
    url(r'^thanks/$', Thanks.as_view(), name='smsregister_thanks'),
    url(r'^unsubscribe/$', Unsubscribe.as_view(), name='smsregister_unsubscribe'),
)
