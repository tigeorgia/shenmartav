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
from .models import Representative



class FeedList (Feed):
    _site = Site.objects.get_current()
    title = _('%s representative feed') % _site.name
    description = _('This is a feed of all %s representatives.') % _site.name

    def link (self):
        return reverse('representative_find')

    def items (self):
        return Representative.objects.all()



class FeedDetail (Feed):
    _site = Site.objects.get_current()
    description = _('This is a detail feed of a %s representative.') % _site.name

    def get_object(self, request, pk):
        self.request = request
        return get_object_or_404(Representative, pk=pk)

    def title (self, obj):
        return _('Representative %s') % obj.name

    def link (self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        protocol = 'http://'
        if hasattr(self, 'request') and self.request.is_secure():
            protocol = 'https://'

        try:
            income_declaration = protocol + self._site.domain +\
                obj.incomedeclaration.all()[0].get_absolute_url()
        except KeyError:
            income_declaration = None

        return _('Party: %(party)s|Unit: %(unit)s|Committee: %(committee)s|Faction: %(faction)s|Is_Majoritarian: %(is_majoritarian)s|Electoral District: %(electoral_district)s|Elected: %(elected)s|Place of Birth: %(pob)s|Family Status: %(family_status)s|Education: %(education)s|Contact Address / Phone: %(contact_address_phone)s|URL: %(url)s|Attendance record: %(attendance_record)s|Salary: %(salary)s|Other Income: %(other_income)s|Expenses: %(expenses)s|Property & Assets: %(property_assets)s|Income declaration URL: %(income_declaration)s|Questions answered: %(answered)s%%') % {
            'party': obj.party.name,
            'unit': obj.unit.name,
            'committee': obj.committee,
            'faction': obj.faction,
            'is_majoritarian': obj.is_majoritarian,
            'electoral_district': obj.electoral_district,
            'elected': obj.elected,
            'pob': obj.pob,
            'family_status': obj.family_status,
            'education': obj.education,
            'contact_address_phone': obj.contact_address_phone,
            'url': obj.url,
            'attendance_record': obj.attendance_record,
            'salary': obj.salary,
            'other_income': obj.other_income,
            'expenses': obj.expenses,
            'property_assets': obj.property_assets,
            'income_declaration': income_declaration,
            'answered': obj.answered
        }

    def item_pubdate (self, obj):
        return datetime.datetime.now()

    def items (self, obj):
        return [obj]
