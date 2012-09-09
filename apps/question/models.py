# vim: set fileencoding=utf-8
"""
Model question

Depends on representative.
"""
__docformat__ = 'epytext en'

import urllib2, copy, datetime

from cms.models.pluginmodel import CMSPlugin
from django.core.mail import EmailMessage
from django.db import models
from django.utils.translation import ugettext as _

from settings import QUESTION_SMS_URL
from representative.models import Representative


class PublicManager (models.Manager):
    """Manager to return public questions."""
    def _clone(self): # bug in Manager? DetailView complains about it missing
        return copy.copy(self)

    def get_query_set(self):
        qs = super(PublicManager, self).get_query_set()
        return qs.filter(is_public=True)



class AnsweredManager (models.Manager):
    """Manager to return answered public questions."""
    def get_query_set(self):
        qs = super(AnsweredManager, self).get_query_set()
        return qs.filter(answer__isnull=False).exclude(answer__exact='')



class Question (models.Model):
    """A question."""
    #: if question is public
    is_public = models.BooleanField(default=False, help_text=_('Is this question public?'))
    #: when the question was asked
    date = models.DateField(default=datetime.datetime.now, help_text=_('When Question was asked'))
    #: first name of the questioner
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'), help_text=_('First Name of the Questioner'))
    #: last name of the questioner
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'), help_text=_('Last Name of the Questioner'))
    #: email address of the questioner
    email = models.CharField(max_length=255, verbose_name=_('Email Address'), help_text=_('Email Address of the Questioner'))
    #: mobile phone number of the questioner
    mobile = models.CharField(blank=True, max_length=255,
        verbose_name=_('Mobile Phone Number'),
        help_text=_('Mobile Phone Number of the Questioner'))
    #: the actual question
    question = models.TextField(verbose_name=_('Question'), help_text=_('The Question'))
    #: the representative being asked
    representative = models.ForeignKey(Representative,
        related_name='questions', verbose_name=_('Representative'),
        help_text=_('Representative being asked'))
    #: the representative's answer
    answer = models.TextField(help_text=_('The Answer'), blank=True, null=True)
    #: parliament.ge response
    parliament_response = models.TextField(blank=True, null=True,
        help_text=_('Response from parliament.ge when sending the question'))

    #: managers
    objects = models.Manager()
    public = PublicManager()
    answered = AnsweredManager()


    class Meta:
        ordering = ['-date', 'is_public']


    @property
    def name (self):
        return self.first_name + ' ' + self.last_name


    def __unicode__ (self):
        try:
            return u'%s %s -> %s: %s' % (self.date, self.name,
                self.representative.name, self.question[:30])
        except Representative.DoesNotExist:
            return u'%s %s -> %s' % (self.date, self.name, self.question[:30])


    @models.permalink
    def get_absolute_url (self, language=None):
        return ('question_detail', [self.pk])


    def _notify_questioner (self):
        """Send a notification to questioner."""
        if self.email:
            subject = _('%(name_asker)s, your question to %(name_representative)s has been answered.' % {
                'name_asker': self.name,
                'name_representative': self.representative.name}
            )
            body = self.question + '\n\n' + self.answer
            msg = EmailMessage(subject=subject, body=body, to=(self.email,))
            msg.send()

        if self.mobile:
            url = QUESTION_SMS_URL.replace('to=', 'to=' + self.mobile).replace(
                'msg=', 'msg=' + urllib2.quote(self.answer))
            try:
                handle = urllib2.urlopen(url)
                response = handle.read()
                handle.close()
            except urllib2.URLError, err:
                pass # silently ignore for the time being
#            else:
#                print 'Response: %s' % response


    def _set_percentage_answered (self):
        """Sets the percentage of questions answered by self's representative."""
        pk = self.representative.pk
        total = Question.public.filter(representative=pk).count()
        two_weeks_ago = datetime.date.today() - datetime.timedelta(14)
        answered = Question.answered.filter(
            representative=pk, date__lt=two_weeks_ago).count()

        try:
            self.representative.answered = (answered * 100.) / total
        except ZeroDivisionError:
            self.representative.answered = 0.
        self.representative.save()


    def save (self, *args, **kwargs):
        try:
            saved = Question.objects.get(pk=self.pk)
            if saved.answer != self.answer and self.answer:
                self._notify_questioner()
        except Question.DoesNotExist:
            pass

        super(Question, self).save(*args, **kwargs)

        if self.is_public:
            self._set_percentage_answered()



# There must be a bug in CMS plugin models. Without exception handler, on
# running an admin command, the class definition would yield:
#  File "/votingrecord/models.py", line 70, in <module>
#      class VotingRecordPluginConf (CMSPlugin):
#        File "/usr/local/lib/python2.7/dist-packages/cms/models/pluginmodel.py", line 56, in __new__
#            table_name = 'cmsplugin_%s' % splitted[1]
#            IndexError: list index out of range
try:
    class QuestionPluginConf (CMSPlugin):
        """Configuration for voting record plugin."""
        #: title of the plugin
        title = models.CharField(max_length=32, default=_('Questions'))
except IndexError:
    pass
