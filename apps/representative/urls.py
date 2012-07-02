from django.conf.urls.defaults import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Find.as_view(), name='representative_find'),
    # name='person' required by popit
    url(r'^representative/(?P<pk>\d+)/(?P<slug>[-\w]+)/$', Detail.as_view(), name='person'),
    url(r'^representative/(?P<pk>\d+)/$', Detail.as_view(), name='representative_pk'),
    url(r'^representative/(?P<slug>[-\w]+)/$', Detail.as_view(), name='representative_slug'),
    url(r'^search/', Search.as_view(), name='representative_search'),

    # AJAX calls answered by HTML
    url(r'^unit/parliament/$', UnitParliament.as_view(), name='unit_parliament'),
    url(r'^unit/ajara/$', UnitAjara.as_view(), name='unit_ajara'),
    url(r'^unit/tbilisi/$', UnitTbilisi.as_view(), name='unit_tbilisi'),
    url(r'^memberinfo/(?P<pk>\d+)/$', MemberInfo.as_view(), name='representative_memberinfo'),
    url(r'^votingrecords/(?P<pk>\d+)/$', VotingRecords.as_view(), name='representative_votingrecords'),

    # AJAX calls answered by JSON
    url(r'^query/(?P<query>.*)/$', query, name='representative_query'),
)
