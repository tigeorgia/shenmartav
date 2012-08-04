"""
URLs for app question
"""
from django.conf.urls.defaults import patterns, url

from .views import List, Ask, Thanks, Detail, Leaderboard, Info, Items, receive
from .feeds import FeedList


urlpatterns = patterns('',
    url(r'^$', List.as_view(), name='question_list'),
    url(r'^ask/$', Ask.as_view(), name='question_ask'),
    url(r'^frage/$', Ask.as_view(), name='question_ask_ka'),
    url(r'^ask/(?P<pk>\d+)/$', Ask.as_view(), name='question_ask_representative'),
    url(r'^frage/(?P<pk>\d+)/$', Ask.as_view(), name='question_ask_representative_ka'),
    url(r'^thanks/$', Thanks.as_view(), name='question_thanks'),
    url(r'^question/(?P<pk>\d+)/$', Detail.as_view(), name='question_detail'),
    url(r'^leaderboard/$', Leaderboard.as_view(), name='question_leaderboard'),
    url(r'^rangliste/$', Leaderboard.as_view(), name='question_leaderboard_ka'),

    # RSS feed
    url(r'^feed/$', FeedList(), name='question_feed_list'),


    # AJAX calls answered by HTML
    url(r'^info/(?P<pk>\d+)/$', Info.as_view(), name='question_info'),
    url(r'^items/(?P<page>\d+)/$', Items.as_view(), name='question_items'),

    # external call from SMS server
    url(r'^receive/(?P<mobile>[-\w]+)/(?P<representative>\d+)/(?P<question>.+)/$',
        receive, name='question_receive'),
)
