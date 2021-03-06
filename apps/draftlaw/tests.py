# -*- coding: utf-8 -*-
"""
Tests for app draftlaw
"""
__docformat__ = 'epytext en'

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.translation import activate

from draftlaw.models import DraftLaw


class DraftLawTest (TestCase):
    fixtures = ['draftlaw_testdata']
    # problem with urls not available in cms apps, so this apps' URLCONF has to
    # be added in ROOT_URLCONF
    # urls = 'draftlaw.urls'

    def test_linked_name (self):
        draftlaw = DraftLaw.objects.get(pk=1)
        self.assertEqual(draftlaw.initiator, draftlaw.initiator_linked)

        activate('en') # guarantee english for comparisons
        draftlaw = DraftLaw.objects.get(pk=6)
        linked = u'<a href="/test/representative/representative/124/teimuraz-tsurtsumia/">Tsurtsumia</a>, Kukava'
        self.assertEqual(draftlaw.initiator_linked, linked)
        linked = u'<a href="/test/representative/representative/124/teimuraz-tsurtsumia/">Tsurtsumia</a>, Zviad Kukava'
        self.assertEqual(draftlaw.author_linked, linked)



    def test_List (self):
        url = reverse('draftlaw_list')
        response = self.client.get(url)
        self.assertContains(response, 'draftlaw')
        self.assertTemplateUsed(response, 'draftlaw/list.html')


    def test_Detail (self):
        url = reverse('draftlaw_detail', args=['07-2397-changes-to-the-tax-code-changes-to-the-law-of-georgia-on-free-industrial-zones'])
        response = self.client.get(url)
        self.assertContains(response, 'draftlaw')
        self.assertTemplateUsed(response, 'draftlaw/detail.html')


    def test_Info (self):
        url = reverse('draftlaw_info', args=[1])
        response = self.client.get(url)
        self.assertContains(response, 'draftlaw')
        self.assertTemplateUsed(response, 'draftlaw/info.html')


    def test_Items (self):
        url = reverse('draftlaw_items', args=[1])
        response = self.client.get(url)
        self.assertContains(response, 'draftlaw')
        self.assertTemplateUsed(response, 'draftlaw/items.html')

        url = reverse('draftlaw_items_query', args=[1, 'zone'])
        response = self.client.get(url)
        self.assertContains(response, 'draftlaw')
        self.assertTemplateUsed(response, 'draftlaw/items.html')
        self.assertContains(response, 'id="item-8"')


    def test_query (self):
        url = reverse('draftlaw_query', args=['zone'])
        response = self.client.get(url)
        self.assertContains(response, '"pk": 8')
