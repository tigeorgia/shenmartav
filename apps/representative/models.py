# vim: set fileencoding=utf-8
"""
Model Representative

Depends on popit
"""
__docformat__ = 'epytext en'

import datetime
#from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.db import models
from django.db.models import Q
try:
    # SIGH! this is Django 1.4 which spits out warnings otherwise
    # Django 1.4. was necessary to fix an issue with PostGIS
    # an issue that occurred with the introduction of unit tests.
    from django.utils.timezone import utc
except ImportError:
    utc = None
from django.utils.translation import activate, get_language, ugettext as _
from django.template.defaultfilters import slugify
from sorl.thumbnail.fields import ImageWithThumbnailsField

import glt
from popit.models import Person, Organisation


#: minimum length of (representative's) name
NAME_MINLEN = 4



class Term (models.Model):
    """A Term during which Representatives are part of a Unit."""
    #: start of the term
    start = models.DateField(blank=False, help_text=_('When term started'))
    #: end of the term
    end = models.DateField(blank=False, help_text=_('When term started'))
    #: name of the term
    name =  models.CharField(max_length=255, blank=False, null=False,
        help_text=_('Name of this term'))

    def __unicode__ (self):
        return u'%s (%s - %s)' % (self.name, self.start, self.end)



class Party (Organisation):
    """A political party in a unit, as used in the template representative/unit.html"""
    #: acronym of this party
    acronym = models.CharField(max_length=16, blank=False, null=False,
        help_text=_('Acronym of this Party'))
    #: url of this representative
    url = models.TextField(blank=True, null=True,
        help_text=_('URL of this Party'))
    #: party logo
    logo = ImageWithThumbnailsField(upload_to='parties',
        thumbnail={'size': (100, 84), 'options': ('crop',)},
        blank=True, null=True, help_text=_('Party logo'))


class Unit (models.Model):
    """A unit/house, like Parliament or Tbilisi City Assembly."""
    #: name of the unit
    name = models.CharField(max_length=255, blank=False, null=False,
        help_text=_('Name of the Unit.'))
    #: short name of the unit, as used in css, etc.
    short = models.CharField(max_length=32, blank=False, null=False,
        help_text=_('Short Name of the Unit, as used in e.g. CSS'))
    #: parties of this unit
    parties = models.ManyToManyField(Party, related_name='unit',
        help_text=_('Parties in this unit'))
    #: unit's active term
    active_term = models.ForeignKey(Term, blank=False, null=True,
        related_name='unit_active',
        help_text=_('The Unit\'s active term.'))
    #: unit's inactive terms
    inactive_terms = models.ManyToManyField(Term, blank=True,
        related_name='unit_inactive',
        help_text=_('Past or just inactive terms served in this Unit.'))


    def __unicode__ (self):
        return u'%s' % self.name



class ParliamentManager (models.Manager):
    """Manager to return Georgian Parliament representatives in active term."""

    def get_query_set(self):
        parliament = Unit.objects.get(pk=1)
        return parliament.active_term.representatives.all()



class TbilisiManager (models.Manager):
    """Manager to return Tbilisi City Hall representatives in active term."""

    def get_query_set(self):
        cityhall = Unit.objects.get(pk=2)
        return cityhall.active_term.representatives.all()



class AjaraManager (models.Manager):
    """Manager to return Ajaran Supreme Council representatives in active term."""

    def get_query_set(self):
        supremecouncil = Unit.objects.get(pk=3)
        return supremecouncil.active_term.representatives.all()





GENDER_CHOICES = (
    (0, _('male')),
    (1, _('female')),
    (2, _('other')),
)

class Representative (Person):
    """A representative derived from popit.Person."""
    #: personal photo
    photo = ImageWithThumbnailsField(upload_to='representatives',
        thumbnail={'size': (200, 168), 'options': ('crop',)},
        blank=True, null=True, help_text=_('Personal Photo'))
    #: party membership
    party = models.ForeignKey(Party, related_name='representatives', null=True,
        help_text=_('Party Membership'))
    #: unit membership
    unit = models.ForeignKey(Unit, related_name='representatives', null=True,
        help_text=_('Unit Membership'))
    #: committee membership
    committee = models.TextField(blank=True, null=True,
        help_text=_('Committee Membership'))
    #: faction membership
    faction = models.TextField(blank=True, null=True,
        help_text=_('Faction Membership'))
    #: is majoritarian?
    is_majoritarian = models.BooleanField(blank=True, default=False,
        help_text=_('Is Majoritarian?'))
    #: electoral district
    electoral_district = models.TextField(blank=True, null=True,
        help_text=_('Electoral District (if Majoritarian)'))
    #: date elected
    elected = models.TextField(blank=True, null=True,
        help_text=_('Date Elected'))
    #: place of birth
    pob = models.TextField(blank=True, null=True,
        help_text=_('Place of Birth'))
    #: family status
    family_status = models.TextField(blank=True, null=True,
        help_text=_('Family Status'))
    #: education
    education = models.TextField(blank=True, null=True,
        help_text=_('Education'))
    #: contact, address and phone number
    contact_address_phone = models.TextField(blank=True, null=True,
        help_text=_('Contact Address / Phone Number'))
    #: salary
    salary = models.FloatField(default=0, null=True,
        help_text=_('== Wages'))
    #: other income
    other_income = models.FloatField(default=0, null=True,
        help_text=_('== Entrepreneurial Income'))
    #: expenses
    expenses = models.TextField(blank=True, null=True,
        help_text=_('Expenses'))
    #: property & assets
    property_assets = models.TextField(blank=True, null=True,
        help_text=_('Property & Assets'))
    #: percentage of questions answered on shenmartav.ge
    answered = models.FloatField(default=0, null=True,
        help_text=_('Percentage of Answered Questions on shenmartav.ge'))
    #: gender of the representative
    gender = models.IntegerField(default=0, choices=GENDER_CHOICES,
        help_text=_('Gender of the Representative'))
    #: terms of the representative
    terms = models.ManyToManyField(Term, blank=True,
        related_name='representatives',
        help_text=_('Terms during which Representative was part of a Unit.'))

    #: managers
    objects = models.Manager()
    parliament = ParliamentManager()
    tbilisi = TbilisiManager()
    ajara = AjaraManager()


    @classmethod
    def _find_firstname_first (cls, name, lang):
        """Find a representative with given name firstname first.

        @param name: name of the representative
        @type name: str
        @param lang: user language
        @type lang: str
        @return: representative matching the name
        @rtype: representative.Representative
        """
        if lang == 'ka':
            firstname_first = glt.firstname_first(name)
        else:
            firstname_first = name.split()[0]

        representative = cls.objects.filter(
            Q(names__name_ka__icontains=firstname_first) |\
            Q(names__name_en__icontains=firstname_first) |\
            Q(names__name__icontains=firstname_first)
        )

        try:
            return representative[0]
        except IndexError:
            return None


    @classmethod
    def _find_lastname_first (cls, name, lang):
        """Find a representative with given name lastname first.

        @param name: name of the representative
        @type name: str
        @param lang: user language
        @type lang: str
        @return: representative matching the name
        @rtype: representative.Representative
        """
        if lang == 'ka':
            lastname_first = glt.lastname_first(name)
        else:
            lastname_first = name.split()[-1]

        representative = cls.objects.filter(
            Q(names__name_ka__icontains=lastname_first) |\
            Q(names__name_en__icontains=lastname_first) |\
            Q(names__name__icontains=lastname_first)
        )

        try:
            return representative[0]
        except IndexError:
            return None


    @classmethod
    def _find_startswith (cls, start):
        """Find a representative whose name starts with given start.

        @param start: first charactes of representative's name
        @type start: str
        @return: representative whose name starts with given start
        @rtype: representative.Representative
        """
        if len(start) < NAME_MINLEN:
            return None

        startswith = start[:NAME_MINLEN]
        representative = cls.objects.filter(
            Q(names__name_ka__istartswith=startswith) |\
            Q(names__name_en__istartswith=startswith) |\
            Q(names__name__istartswith=startswith)
        )

        try:
            return representative[0]
        except IndexError:
            return None


    @classmethod
    def find (cls, name):
        """Find a representative with given name.

        @param name: name of the representative
        @type name: str
        @return: representative matching the name
        @rtype: representative.Representative
        """
        if len(name) < NAME_MINLEN: return None
        lang = get_language()[:2]

        representative = cls.objects.filter(
            Q(names__name_ka__icontains=name) |\
            Q(names__name_en__icontains=name) |\
            Q(names__name__icontains=name)
        )
        if representative: return representative[0]

        representative = cls._find_firstname_first(name, lang)
        if representative: return representative

        representative = cls._find_lastname_first(name, lang)
        if representative: return representative

        splitname = name.split()
        representative = cls._find_startswith(splitname[0])
        if representative: return representative

        if len(splitname) > 1:
            representative = cls._find_startswith(splitname[-1])
            if representative: return representative

        return None


    @classmethod
    def by_lastname_firstname_first (cls, representatives=None):
        """Sort given representatives by lastname and show firstname first.

        @param representatives: queryset of representatives to sort, using all() if None
        @type representatives: QuerySet
        @return: sorted list by lastname, including 'firstname_first'
        @rtype: [{
            'pk': int, 'slug': str, 'party__acronym': str,
            'is_majoritarian': bool, 'photo': str,
            'names__name': str, 'names__name_$lang': str,
            'firstname_first': str
        }]
        """
        if representatives is None: # != []
            representatives = cls.objects.all()

        by_lastname = {}
        # losing language abstraction, gaining massive reduction in db queries
        name_lang = 'names__name_' + get_language()[:2]
        reps = representatives.values('pk', 'slug',
            'party__acronym', 'is_majoritarian', 'photo',
            'names__name', name_lang)
        for r in reps:
            try:
                lastname = r[name_lang].split()[-1]
                r['firstname_first'] = r[name_lang]
            except AttributeError:
                lastname = r['names__name'].split()[-1]
                r['firstname_first'] = r['names__name']
            by_lastname[lastname] = r

        return [by_lastname[key] for key in sorted(by_lastname.keys())]


    @classmethod
    def by_lastname_lastname_first (cls, representatives=None, choices=False):
        """Sort given representatives by lastname and show lastname first.

        @param representatives: queryset of representatives to sort, using all() if None
        @type representatives: QuerySet
        @param choices: if list suitable for form choices should be returned
        @type choices: bool
        @return: sorted list by lastname, including 'lastname_first'
        @rtype: [{
            'pk': int, 'slug': str,
            'names_name': str, 'names__name_$lang': str,
            'lastname_first': str
        }]

        """
        if representatives is None: # != []
            representatives = cls.objects.all()

        by_lastname = {}
        # losing language abstraction, gaining massive reduction in db queries
        name_lang = 'names__name_' + get_language()[:2]
        reps = representatives.values('pk', 'slug', 'names__name', name_lang)
        for r in reps:
            try:
                splitname = r[name_lang].split()
            except AttributeError:
                splitname = r['names__name'].split()
            lastname = splitname.pop()
            r['lastname_first'] = lastname + ' ' + ' '.join(splitname)
            by_lastname[lastname] = r

        if choices:
            return [
                (by_lastname[key]['pk'], by_lastname[key]['lastname_first'])
                for key in sorted(by_lastname.keys())
            ]
        else:
            return [by_lastname[key] for key in sorted(by_lastname.keys())]


    @property
    def income (self):
        try:
            base = int(settings.BASE_INCOME[self.unit.short])
        except (AttributeError, KeyError, ValueError):
            base = 0

        additional = int(self.salary - base)
        if additional < 0:
            additional = int(self.salary) # salary in declaration doesn't include base

        return {
            'total': int(base + additional + self.other_income),
            'base': base,
            'additional': additional,
            'other': int(self.other_income),
        }


    def save (self, *args, **kwargs):
        # enforce rewriting of slug in default language
        lang = get_language()
        activate(settings.LANGUAGE_CODE)
        self.slug = slugify(str(self.name))
        activate(lang)

        super(Representative, self).save(*args, **kwargs)



class AdditionalInformation (models.Model):
    #: representative this info belongs to
    representative = models.ForeignKey(Representative,
        related_name='additional_information', null=True,
        help_text=_('Representative'))
    #: value of this info
    value = models.TextField(null=True, help_text=_('Additional Information'))

    def __unicode__ (self):
        return u'%s: %s' % (str(self.representative.name), self.value)



class Url (models.Model):
    """Urls belonging to a representative."""
    #: representative this url belongs to
    representative = models.ForeignKey(Representative,
        related_name='urls', null=True,
        help_text=_('Representative'))
    #: label of this url
    label = models.CharField(max_length=255, blank=False, default=_('Homepage'),
        help_text=_('Label for this Url, e.g. Homepage, Facebook, Twitter, etc.'))
    #: the actual url; text field because georgian urls can become very long
    url = models.TextField(blank=False, help_text=_('The URL'))

    def __unicode__ (self):
        return u'%s: %s - %s' % (str(self.representative.name), self.label, self.url)



ATTENDANCE_GROUP_CHOICES = (
    (0, _('very low')),
    (1, _('low')),
    (2, _('ordinary')),
    (3, _('high')),
    (4, _('very high')),
)

class Attendance (models.Model):
    """A representative's attendance record."""
    #: number of attended votes
    attended = models.IntegerField(default=0,
        help_text=_('Number of Attended Votes'))
    #: pre-calculated percentage of attended votes
    percentage_attended = models.IntegerField(default=0,
        help_text=_('Pre-calculated Percentage of Attended Votes'))
    #: number of absent votes
    absent = models.IntegerField(default=0,
        help_text=_('Number of Absent Votes'))
    #: pre-calculated percentage of absent votes
    percentage_absent = models.IntegerField(default=0,
        help_text=_('Pre-calculated Percentage of Absent Votes'))
    #: pre-calculated number of total votes
    total = models.IntegerField(default=0,
        help_text=_('Number of Pre-calculated Total Votes'))
    #: attendance group
    group = models.IntegerField(default=0,
        choices=ATTENDANCE_GROUP_CHOICES,
        help_text=_('Voting Attendance in Relation to other Representatives'))
    #: representative this attendance record belongs to
    representative = models.ForeignKey(Representative,
        null=False, related_name='attendance',
        help_text=_('Representative'))

    def __unicode__ (self):
        return u'%s: %s/%s' % (str(self.representative.name),
            str(self.attended), str(self.total))



class RandomRepresentative (models.Model):
    """Defines the randomly selected representative of the day."""
    #: date when the current random representative was set
    date_set = models.DateTimeField(help_text=_('When random representative was set'))
    #: random representative
    representative = models.ForeignKey(Representative,
        null=True, help_text=_('Random Representative'))


    @classmethod
    def get(cls):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        date_set = datetime.datetime(
            now.year, now.month, now.day, 0, 0).replace(tzinfo=utc)

        try:
            rr = RandomRepresentative.objects.all()[0]
            if (now - rr.date_set).days >= 1:
                rr.date_set = date_set
                try:
                    rr.representative = Representative.parliament.order_by('?')[0]
                    rr.save()
                except IndexError:
                    pass
        except IndexError:
            try:
                representative = Representative.parliament.order_by('?')[0]
            except IndexError:
                representative = None

            rr = RandomRepresentative(date_set=date_set,
                representative=representative)
            rr.save()


        return rr.representative


    def __unicode__ (self):
        if self.representative:
            return u'%s' % self.representative.name
        else:
            return _('Unknown')



# There must be a bug in CMS plugin models. Without exception handler, on
# running an admin command, the class definition would yield:
#  File "/votingrecord/models.py", line 70, in <module>
#      class VotingRecordPluginConf (CMSPlugin):
#        File "/usr/local/lib/python2.7/dist-packages/cms/models/pluginmodel.py", line 56, in __new__
#            table_name = 'cmsplugin_%s' % splitted[1]
#            IndexError: list index out of range
#class RepresentativePluginConf (CMSPlugin):
#    """Configuration for Representative plugin."""
#    #: title of the plugin
#    title = models.CharField(max_length=32, default=_('Representative'))
