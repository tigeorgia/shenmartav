# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PodcastingApp(CMSApp):
    name = _("Podcasting App")
    urls = ["podcasting.urls"]

apphook_pool.register(PodcastingApp)
