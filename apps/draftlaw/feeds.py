# -*- coding: utf-8 -*-

"""
Feed draftlaw
"""
__docformat__ = 'epytext en'

import datetime
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _

from settings import NUM_FEEDITEMS
from .models import DraftLaw



class FeedList (Feed):
    _site = Site.objects.get_current()
    title = _('%s draftlaw feed') % _site.name
    description = _('This is a feed of %s draftlaws.') % _site.name

    def link (self):
        return reverse('draftlaw_list')

    def items (self):
        return DraftLaw.objects.all().order_by('-bureau_date')[:NUM_FEEDITEMS]

    def item_pubdate (self, obj):
        return datetime.datetime.combine(obj.bureau_date, datetime.time())



class FeedDetail (Feed):
    _site = Site.objects.get_current()
    description = _('This is a detail feed of a %s draftlaw.') % _site.name

    def get_object(self, request, pk):
        return get_object_or_404(DraftLaw, pk=pk)

    def title (self, obj):
        return _('Draftlaw %s') % obj.title

    def link (self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return _('Introduced: %(introduced)s|Title: %(title)s|Initiator: %(initiator)s|Author: %(author)s|Status: %(status)s|Summary: %(summary)s|Full-text URL: %(full_text_url)s|Enacted-text URL: %(enacted_text_url)s|Law Number: %(law_number)s') % {
            'introduced': obj.bureau_date,
            'title': obj.title,
            'initiator': obj.initiator,
            'author': obj.author,
            'status': obj.status,
            'summary': obj.summary,
            'full_text_url': obj.full_text_url,
            'enacted_text_url': obj.enacted_text_url,
            'law_number': obj.law_number
        }

    def item_pubdate (self, obj):
        return datetime.datetime.combine(obj.bureau_date, datetime.time())

    def items (self, obj):
        return [obj]
