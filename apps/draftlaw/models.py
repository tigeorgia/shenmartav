# vim: set fileencoding=utf-8
"""
Model draftlaw

Depends on votingrecord and representative.
"""
__docformat__ = 'epytext en'

import datetime
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import get_language, ugettext_lazy as _

from glt import slughifi
from votingrecord.models import VotingRecord
from representative.models import Representative



class DraftLaw (models.Model):
    """A draft/passed law."""
    SHORTSTATUS_CHOICES = (
        ('P', _('Passed')),
        ('D', _('Draft')),
    )

    slug = models.SlugField(max_length=100, editable=False, null=False)
    #: date of introduction
    bureau_date = models.DateField(help_text=_('Draft Law\'s Bureau Date'))
    #: bill number
    bill_number = models.CharField(max_length=255, help_text=_('Bill Number of the Draft Law'))
    #: title of the law
    title = models.TextField(help_text=_('Title of the Draft Law'))
    #: entity initiating the draft
    initiator = models.TextField(blank=True, help_text=_('Initiator'))
    #: person authoring the draft
    author = models.TextField(blank=True, help_text=_('Author'))
    #: status of the law, e.g. '1st Hearing Economy Pass'
    status = models.CharField(max_length=255, help_text=_('Status of the Draft Law'))
    #: short status of the law; in one word
    shortstatus = models.CharField(max_length=1, default='D', choices=SHORTSTATUS_CHOICES, help_text=_('Short Status of the Draft Law'))
    #: summary of the law
    summary = models.TextField(help_text=_('Summary'), blank=True)
    #: full text of the law
    full_text = models.TextField(help_text=_('Full Text'), blank=True)
    #: URL of the full text of the law
    full_text_url = models.CharField(max_length=255,
        help_text=_('Full Text URL'), blank=True)
    #: URL of the text of the enacted law
    enacted_text_url = models.CharField(max_length=255,
        help_text=_('Enacted Text URL'), blank=True)
    #: enacted law number
    law_number = models.CharField(max_length=255, blank=True, null=True,
        help_text=_('Number of the Enacted Law'))
    #: voting record of the enacted law
    voting_record = models.ForeignKey(VotingRecord, related_name='voting_on',
        help_text=_('Voting Record'), blank=True, null=True)
    #: related document 1
    related_1 = models.FileField(upload_to='draftlaw', help_text=_('Related Document 1'), blank=True)
    #: related document 2
    related_2 = models.FileField(upload_to='draftlaw', help_text=_('Related Document 2'), blank=True)
    #: related document 3
    related_3 = models.FileField(upload_to='draftlaw', help_text=_('Related Document 3'), blank=True)
    #: related document 4
    related_4 = models.FileField(upload_to='draftlaw', help_text=_('Related Document 4'), blank=True)
    #: related document 5
    related_5 = models.FileField(upload_to='draftlaw', help_text=_('Related Document 5'), blank=True)
    #: for moderation
    enable_annotations = models.BooleanField(default=True, editable=False)
    moderate_annotations = models.DateField(default=datetime.date.today, editable=False)


    class Meta:
        ordering = ('-bill_number',)


    def save (self, *args, **kwargs):
        max_len = self._meta.get_field('slug').max_length
        self.slug = slughifi(str(self)[:max_len])
        super(DraftLaw, self).save(*args, **kwargs)


    def __unicode__ (self):
        return u'%s %s' % (self.bill_number, self.title)


    @models.permalink
    def get_absolute_url (self, language=None):
        return ('draftlaw_detail', [self.slug])


    def _linked_name (self, attr_base):
        """Looks for representative's names in given attribute and adds links to them.

        @param attr_base: basename of the attribute to get the name from
        @type attr_base: str
        @return: item with properly linked representative(s)
        @rtype: str
        """
        try:
            name = getattr(self, attr_base + '_' + get_language()[:2])
        except AttributeError:
            try:
                name = getattr(self, attr_base)
            except AttributeError:
                return None

        linked = name.split('(')[0]
        if linked.lower().startswith('mp '):
            linked = linked[3:]
        if linked.lower().startswith('mps '):
            linked = linked[4:]

        splitnames = linked.split(',')
        if len(splitnames) == 1:
            splitnames = linked.split(';')
        names = [n.strip() for n in splitnames]

        linked = []
        for name in names:
                representative = Representative.find(name)
                if representative:
                    linked.append('<a href="%s">%s</a>' % (
                        representative.get_absolute_url(), name))
                else:
                    linked.append(name)


        return ', '.join(linked)



    @property
    def initiator_linked (self):
        return self._linked_name('initiator')

    @property
    def author_linked (self):
        return self._linked_name('author')



from django.contrib.comments.moderation import CommentModerator, moderator
class DraftLawModerator (CommentModerator):
    email_notification = True
    enable_field = 'enable_annotations'
    auto_moderate_field = 'moderate_annotations'
    moderate_after = 0 # immediately
moderator.register(DraftLaw, DraftLawModerator)



class DraftLawDiscussion (models.Model):
    """Discussion about a law."""
    #: law being discussed
    draftlaw = models.ForeignKey(DraftLaw, related_name='discussions', help_text=_('Draft Law'))
    #: date of discussion
    date = models.DateField(help_text=_('Date of Discussion'))
    #: place of discussion
    place = models.CharField(max_length=255, help_text=_('Place of Discussion'))
    #: stage of the discussion: [0..5]
    stage = models.IntegerField(default=0,
        help_text=_('Stage of the Discussion in Terms of Draft Law Completion'))

    def __unicode__ (self):
        return '%s %s (%s)' % (self.draftlaw.bill_number, self.draftlaw.title, self.place)



class DraftLawChild (models.Model):
    """Draft laws are introduced as a package and seperate laws might become enacted from that."""
    #: the parent draft law
    parent = models.ForeignKey(DraftLaw, related_name='children', help_text=_('Parent Draft Law'))
    #: bill number
    bill_number = models.CharField(max_length=255, help_text=_('Bill Number of the Draft Law'))
    #: title of the law
    title = models.TextField(help_text=_('Title of the Draft Law'))
    #: URL of the text of the enacted law
    enacted_text_url = models.CharField(max_length=255, blank=True,
        help_text=_('Enacted Text URL'))
    #: enacted law number
    law_number = models.CharField(max_length=255, blank=True, null=True,
        help_text=_('Number of the Enacted Law'))
    #: voting record of the enacted law
    voting_record = models.ForeignKey(VotingRecord, related_name='voting_on_child',
        help_text=_('Voting Record'), blank=True, null=True)

    def __unicode__ (self):
        return '%s %s' % (self.bill_number, self.title)



# There must be a bug in CMS plugin models. Without exception handler, on
# running an admin command, the class definition would yield:
#  File "/votingrecord/models.py", line 70, in <module>
#      class VotingRecordPluginConf (CMSPlugin):
#        File "/usr/local/lib/python2.7/dist-packages/cms/models/pluginmodel.py", line 56, in __new__
#            table_name = 'cmsplugin_%s' % splitted[1]
#            IndexError: list index out of range
try:
    class DraftLawPluginConf (CMSPlugin):
        """Configuration for draftlaw plugin."""
        #: title of the plugin
        title = models.CharField(max_length=32, default=_('Draft Laws'))
except IndexError:
    pass
