# -*- coding: utf-8 -*
"""
Tests for app incomedeclaration
"""
__docformat__ = 'epytext en'

from django.core.urlresolvers import reverse
from django.test import TestCase

from incomedeclaration.models import IncomeDeclaration


class IncomeDeclarationTest (TestCase):
    fixtures = ['incomedeclaration_testdata']
    # problem with urls not available in cms apps, so this apps' URLCONF has to
    # be added in ROOT_URLCONF
    # urls = 'incomedeclaration.urls'

    def test_unicode(self):
        decl = IncomeDeclaration()
        decl.decl_id = 1
        decl.name = 'name'

        self.assertEqual(str(decl), str(decl.decl_id) + ' ' + decl.name)



    def test_List (self):
        url = reverse('incomedeclaration_list')
        response = self.client.get(url)
        self.assertContains(response, 'incomedeclaration')
        self.assertTemplateUsed(response, 'incomedeclaration/list.html')



    def test_Detail (self):
        url = reverse('incomedeclaration_detail', args=['000039-paata-lezhava'])
        response = self.client.get(url)
        self.assertContains(response, 'incomedeclaration')
        self.assertTemplateUsed(response, 'incomedeclaration/detail.html')
