# -*- coding: utf-8 -*-

"""
URLs draftlaw
"""
__docformat__ = 'epytext en'

from django.conf.urls.defaults import patterns, url

from .views import Page


urlpatterns = patterns('',
    # AJAX calls answered by HTML
    url(r'^page/(?P<page>\d+)/$', Page.as_view(), name='smsalert_page'),
)
