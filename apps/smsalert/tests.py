# -*- coding: utf-8 -*
"""
Tests for app smsalert
"""
__docformat__ = 'epytext en'

from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import SMSAlert


class SMSAlertTest (TestCase):
    fixtures = ['smsalert_testdata']
    # problem with urls not available in cms apps, so this apps' URLCONF has to
    # be added in ROOT_URLCONF
    # urls = 'draftlaw.urls'


    def test_Page (self):
        url = reverse('smsalert_page', args=[1])
        response = self.client.get(url)
        self.assertContains(response, 'alert')
        self.assertTemplateUsed(response, 'smsalert/page.html')
