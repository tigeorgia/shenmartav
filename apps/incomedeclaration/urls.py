from django.conf.urls.defaults import patterns, include, url
from .views import Detail, List

urlpatterns = patterns('',
    url(r'^$', List.as_view(), name='incomedeclaration_list'),
    url(r'^declaration/(?P<slug>[-\w]+)/$', Detail.as_view(), name='incomedeclaration_detail'),
)
