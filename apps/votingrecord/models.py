# vim: set fileencoding=utf-8
"""
Model votingrecord
"""
__docformat__ = 'epytext en'

from cms.models.pluginmodel import *
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q

from glt import slughifi



class VotingRecord (models.Model):
    """A voting record."""
    slug = models.SlugField(max_length=100, editable=False, null=False)
    #: Parliament.ge kan (?) ID
    kan_id = models.IntegerField(null=True, help_text=_('kan ID'))
    #character portion of the ID
    kan_id_chars = models.CharField(max_length=512, null=True)

    #: scrape date
    scrape_date = models.DateField(null=True, editable=False,
        help_text=('Date of Scrape Process'))
    #: name of the bill
    name = models.CharField(max_length=512, null=True,
        help_text=_('Name of the Bill'))
    #: voting date
    date = models.DateField(null=True, help_text=_('Date of Voting'))
    #: url where to find the voting record
    url = models.CharField(max_length=255, null=True, help_text=_('URL of the Voting Record'))
    #: bill number
    number = models.CharField(max_length=32, null=True, help_text=_('Bill Number'))
    #: amended by these records
    amended_by = models.ManyToManyField('self',
        null=True,  symmetrical=False, related_name='amending',
        help_text=_('Amended by these Voting Records'))


    class Meta:
        ordering = ['-date', '-number']


    def save (self, *args, **kwargs):
        max_len = self._meta.get_field('slug').max_length
        self.slug = slughifi(str(self)[:max_len])
        super(VotingRecord, self).save(*args, **kwargs)


    def __unicode__ (self):
        return u'%s %s' % (self.number, self.name)


    @models.permalink
    def get_absolute_url (self, language=None):
        return ('votingrecord_detail', [self.id])


class VotingRecordResult (models.Model):
    """A voting result."""
    #: voting record ID
    record = models.ForeignKey(VotingRecord, related_name='results',
        help_text=_('Voting Record'))

    #: voting session number
    session = models.IntegerField(null=True)
    
    #: total voting session (3 or 1 session(s) required for a law to be voted)
    totalsession = models.IntegerField(null=True)
    
    #: vote value
    vote = models.CharField(max_length=32, help_text=_('Vote Value'))
    #: representative's name
    name = models.CharField(max_length=255,
        help_text=_('Representative\'s Name'))
    #: representative
    representative = models.ForeignKey("representative.Representative", null=True,
        related_name='votingresults',
        help_text=_('Representative voting on this'))
    #: CSS class for color display
    css = models.CharField(max_length=32, null=True,
        help_text=_('CSS class for color display'))


    class Meta:
        ordering = ['-vote']


    @classmethod
    def get_counts (cls, record=None, representative=None,session=None,lawcount=False):
        """Get counts of the four voting record result possibilities.

        Either for the given voting record or for the given representative.
        Supplying both will return None.

        @param record: voting record to get counts for
        @type record: votingrecord.VotingRecord
        @param representative: representative to get counts for
        @type representative: representative.Representative
        @return: dict with voting record result counts
        @rtype: { 'yes': int, 'no': int, 'abstention': int, 'absent': int, 'total': int }
        """
        if record and representative:
            return None
        if record:
            results = cls.objects.filter(record=record)
        elif representative:
            results = cls.objects.filter(representative=representative)
        else:
            return None

        if session:
            results = results.filter(session=session)
            
        if lawcount:
            results = results.filter(Q(session=3,totalsession=3) | Q(session=1,totalsession=1))

        return {
            'yes': results.filter(vote=u'დიახ').count(),
            'no': results.filter(vote=u'არა').count(),
            'abstained': results.filter(vote=u'არ მიუცია').count(),
            'absent': results.filter(vote=u'არ ესწრებოდა').count(),
            'total': results.count(),
        }


    def __unicode__ (self):
        return '%s %s' % (self.name, self. vote)



class VotingRecordAmendment (models.Model):
    """An amendment to a voting record."""
    #: voting record ID
    record = models.ForeignKey(VotingRecord, related_name='amendments',
        help_text=_('Voting Record'))
    #: bill number
    number = models.CharField(max_length=32, null=True,
        help_text=_('Bill Number'))

    def __unicode__ (self):
        return '%s > %s %s' % (self.number, self.record.number, self.record.name)



# There must be a bug in CMS plugin models. Without exception handler, on
# running an admin command, the class definition would yield:
#  File "/votingrecord/models.py", line 70, in <module>
#      class VotingRecordPluginConf (CMSPlugin):
#        File "/usr/local/lib/python2.7/dist-packages/cms/models/pluginmodel.py", line 56, in __new__
#            table_name = 'cmsplugin_%s' % splitted[1]
#            IndexError: list index out of range
try:
    class VotingRecordPluginConf (CMSPlugin):
        """Configuration for voting record plugin."""
        #: title of the plugin
        title = models.CharField(max_length=32, default=_('Voting Records'))
except IndexError:
    pass
