from django.conf.urls.defaults import patterns, url
from .views import *
from .feeds import FeedList, FeedDetail


urlpatterns = patterns('',
    url(r'^$', Find.as_view(), name='representative_find'),
    # name='person' required by popit
    url(r'^representative/(?P<pk>\d+)/(?P<slug>[-\w]+)/$', Detail.as_view(), name='person'),
    url(r'^representative/(?P<pk>\d+)/$', Detail.as_view(), name='representative_pk'),
    url(r'^representative/(?P<slug>[-\w]+)/$', Detail.as_view(), name='representative_slug'),
    url(r'^search/', Search.as_view(), name='representative_search'),

    # RSS feed
    url(r'^feed/$', FeedList(), name='representative_feed_list'),
    url(r'^feed/(?P<pk>\d+)/$', FeedDetail(), name='representative_feed_detail'),

    # AJAX calls answered by HTML
    url(r'^unit/parliament/$', UnitParliament.as_view(), name='unit_parliament'),
    url(r'^unit/ajara/$', UnitAjara.as_view(), name='unit_ajara'),
    url(r'^unit/tbilisi/$', UnitTbilisi.as_view(), name='unit_tbilisi'),
    url(r'^info/(?P<pk>\d+)/$', Info.as_view(), name='representative_info'),
    url(r'^votingrecords/(?P<pk>\d+)/$', VotingRecords.as_view(), name='representative_votingrecords'),

    # AJAX calls answered by JSON
    url(r'^query/(?P<query>.*)/$', query, name='representative_query'),
)
