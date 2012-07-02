from django.conf.urls.defaults import patterns, url
from .views import Detail, List

urlpatterns = patterns('',
    url(r'^$', List.as_view(), name='votingrecord_list'),
    url(r'^record/(?P<slug>[-\w]+)/$', Detail.as_view(), name='votingrecord_detail'),
)
