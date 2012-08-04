# -*- coding: utf-8 -*
"""
Tests for app representative
"""
__docformat__ = 'epytext en'

import datetime
from django.utils.timezone import utc

from django.core.urlresolvers import reverse
from django.test import TestCase

from representative.models import Representative, RandomRepresentative, NAME_MINLEN
from representative.views import UnitParliament, Detail
from question.models import Question


class RepresentativeTest (TestCase):
    fixtures = ['representative_testdata']
    # problem with urls not available in cms apps, so this apps' URLCONF has to
    # be added in ROOT_URLCONF
    # urls = 'representative.urls'

    def test_Find (self):
        url = reverse('representative_find')
        response = self.client.get(url)
        self.assertContains(response, 'representative')
        self.assertTemplateUsed(response, 'representative/find.html')


    def test_Detail_get_questions (self):
        d = Detail()

        r = Representative.objects.get(pk=3)
        questions = {
            'answered': {'absolute': 0, 'relative': 0},
            'noresponse': {'absolute': 0, 'relative': 0},
            'last': []
        }
        self.assertEqual(d._get_questions(r), questions)

        r = Representative.objects.get(pk=1)
        q = Question.objects.get(pk=2)
        questions = {
            'answered': {'absolute': 1, 'relative': 50.0},
            'noresponse': {'absolute': 1, 'relative': 50.0},
            'last': q
        }
        self.assertEqual(d._get_questions(r), questions)


    def test_DetailPerson (self):
        url = reverse('person', args=[1, 'abulashvili-nugzari'])
        response = self.client.get(url)
        self.assertContains(response, 'representative')
        self.assertTemplateUsed(response, 'representative/detail.html')


    def test_DetailPk (self):
        url = reverse('representative_pk', args=[1])
        response = self.client.get(url)
        self.assertContains(response, 'representative')
        self.assertTemplateUsed(response, 'representative/detail.html')


    def test_DetailSlug (self):
        url = reverse('representative_slug', args=['abulashvili-nugzari'])
        response = self.client.get(url)
        self.assertContains(response, 'representative')
        self.assertTemplateUsed(response, 'representative/detail.html')


    def test_Search (self):
        url = reverse('representative_search')
        response = self.client.get(url)
        self.assertContains(response, u'Search')
        self.assertTemplateUsed(response, 'representative/search.html')


    def test_Unit_get_members (self):
        up = UnitParliament()
        members = [13, 2, 8, 5, 4, 7, 3, 1, 9]
        members_up = up._get_members()
        for i in xrange(len(members_up)):
            self.assertEqual(members_up[i]['pk'], members[i])


    def test_UnitParliament (self):
        url = reverse('unit_parliament')
        response = self.client.get(url)
        self.assertContains(response, 'abulashvili-nugzari')
        self.assertTemplateUsed(response, 'representative/unit.html')


    def test_UnitAjara (self):
        url = reverse('unit_ajara')
        response = self.client.get(url)
        self.assertContains(response, '')
        self.assertTemplateUsed(response, 'representative/unit.html')


    def test_UnitTbilisi (self):
        url = reverse('unit_tbilisi')
        response = self.client.get(url)
        self.assertContains(response, '')
        self.assertTemplateUsed(response, 'representative/unit.html')


    def test_info (self):
        url = reverse('representative_info', args=[1])
        response = self.client.get(url)
        self.assertContains(response, u'აბულაშვილი ნუგზარი')
        self.assertTemplateUsed(response, 'representative/info.html')


    def test_Votingrecords (self):
        url = reverse('representative_votingrecords', args=[1])
        response = self.client.get(url)
        self.assertContains(response, '')
        self.assertTemplateUsed(response, 'representative/votingrecords.html')


    def test_query (self):
        url = reverse('representative_query', args=[u'აბულაშვილი ნუგზარი'])
        response = self.client.get(url)
        self.assertContains(response, '"pk": 1')


    def test_Representative_find (self):
        name = u'idontexistinthisdatabase'
        self.assertEqual(Representative.find(name), None)

        name = u'აბულაშვილი ნუგზარი'
        self.assertNotEqual(Representative.find(name), None)

        name = u'ნუგზარ აბულაშვილი'
        self.assertNotEqual(Representative.find(name), None)

        name = u'აბულაშვილი'
        self.assertNotEqual(Representative.find(name), None)

        name = u'ნუგზარი'
        self.assertNotEqual(Representative.find(name), None)

        name = u'ნუგზარ'
        self.assertNotEqual(Representative.find(name), None)

        name = name[:NAME_MINLEN]
        self.assertNotEqual(Representative.find(name), None)

        name = name[:-1]
        self.assertEqual(Representative.find(name), None)


    def test_Representative_total_income (self):
        r = Representative.objects.all()[0]
        self.assertEqual(r.total_income, 49272)

        r = Representative.objects.all()[1]
        self.assertEqual(r.total_income, 69572)


    def test_Representative_attendance (self):
        r = Representative.objects.all()[0]
        self.assertEqual(r.attendance_record, '641/791 (81.0%)')

        result = {
            'absent': 150, 'attended': 641, 'percentage': u'81.0%', 'total': 791
        }
        self.assertEqual(r.attendance, result)



class RandomRepresentativeTest (TestCase):
    fixtures = ['representative_testdata']


    def test_get  (self):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        current = RandomRepresentative.objects.all()[0]
        days_passed = (now - current.date_set).days
        rr = RandomRepresentative.get()

        if  days_passed >= 1:
            self.assertNotEqual(current.representative.pk, rr.pk)
        else:
            self.assertEqual(current.representative.pk, rr.pk)
