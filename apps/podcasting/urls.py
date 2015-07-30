# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from apps.podcasting.views import ShowListView, ShowDetailView, EpisodeListView, EpisodeDetailView, AllEpisodesListView


urlpatterns = patterns("",
    url(r"^$", AllEpisodesListView.as_view(),
        name="podcasting_all_episodes_list"),
    url(r"^show/$", ShowListView.as_view(),
        name="podcasting_show_list"),
    url(r"^(?P<slug>[-\w]+)/$", ShowDetailView.as_view(),
        name="podcasting_show_detail"),
    url(r"^(?P<show_slug>[-\w]+)/archive/$", EpisodeListView.as_view(),
        name="podcasting_episode_list"),
    url(r"^(?P<show_slug>[-\w]+)/(?P<slug>[-\w]+)/$", EpisodeDetailView.as_view(),
        name="podcasting_episode_detail"),
)
