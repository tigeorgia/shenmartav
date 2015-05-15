# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns("",
    url(r"^podcasts/", include("podcasting.urls")),
    )
