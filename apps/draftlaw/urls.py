"""
URLs draftlaw
"""
__docformat__ = 'epytext en'

from django.conf.urls.defaults import patterns, url

from .views import List, Detail, Info, Items, query
from .feeds import FeedList, FeedDetail


urlpatterns = patterns('',
    url(r'^$', List.as_view(), name='draftlaw_list'),
    url(r'^draftlaw/(?P<slug>[-\w]+)/$', Detail.as_view(), name='draftlaw_detail'),

    # RSS feed
    url(r'^feed/$', FeedList(), name='draftlaw_feed_list'),
    url(r'^feed/(?P<pk>\d+)/$', FeedDetail(), name='draftlaw_feed_detail'),

    # AJAX calls answered by HTML
    url(r'^info/(?P<pk>\d+)/$', Info.as_view(), name='draftlaw_info'),
    url(r'^items/(?P<page>\d+)/$', Items.as_view(), name='draftlaw_items'),
    url(r'^items/(?P<page>\d+)/(?P<query>.*)/$', Items.as_view(), name='draftlaw_items_query'),

    # AJAX calls answered by JSON
    url(r'^query/(?P<query>.*)/$', query, name='draftlaw_query'),
)
