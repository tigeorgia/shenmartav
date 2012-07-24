# -*- coding: utf-8 -*
"""
Tests for app votingrecord
"""
__docformat__ = 'epytext en'

from django.core.urlresolvers import reverse
from django.test import TestCase

from votingrecord.models import VotingRecord, VotingRecordResult
from representative.models import Representative


class VotingRecordTest (TestCase):
    fixtures = ['votingrecord_testdata']
    # problem with urls not available in cms apps, so this apps' URLCONF has to
    # be added in ROOT_URLCONF
    # urls = 'votingrecord.urls'

    def test_unicode(self):
        vr = VotingRecord()
        vr.number = '1234-IS'
        vr.name = 'name'

        self.assertEqual(str(vr), vr.number + ' ' + vr.name)


    def test_List (self):
        url = reverse('votingrecord_list')
        response = self.client.get(url)
        self.assertContains(response, 'votingrecord')
        self.assertTemplateUsed(response, 'votingrecord/list.html')


    def test_Detail (self):
        url = reverse('votingrecord_detail', args=['none-sakartvelos-organuli-kanoni-sakar'])
        response = self.client.get(url)
        self.assertContains(response, 'votingrecord')
        self.assertTemplateUsed(response, 'votingrecord/detail.html')


    def test_get_votecounts (self):
        vr = VotingRecord.objects.get(pk=1110)
        counts = {'abstained': 0, 'yes': 0, 'total': 0, 'absent': 0, 'no': 0}
        self.assertEqual(VotingRecordResult.get_counts(record=vr), counts)

        r = Representative.objects.get(pk=2)
        self.assertEqual(VotingRecordResult.get_counts(representative=r), counts)

        vr = VotingRecord.objects.get(pk=136)
        counts = {'abstained': 0, 'yes': 1, 'total': 4, 'absent': 0, 'no': 3}
        self.assertEqual(VotingRecordResult.get_counts(record=vr), counts)

        r = Representative.objects.get(pk=1)
        self.assertEqual(VotingRecordResult.get_counts(representative=r), counts)

