# vim: set fileencoding=utf-8
"""
Model smsalert

Depends on draftlaw.
"""
__docformat__ = 'epytext en'


import datetime
from django.db import models
from django.utils.translation import get_language, ugettext_lazy as _

from draftlaw.models import DraftLaw



class SMSAlert (models.Model):
    """An SMSAlert about Parliament activities."""

    # text of the SMS alert
    text = models.TextField(help_text=_('SMS Alert text'), blank=False)
    # date when alert was sent
    date_sent = models.DateField(help_text=_('When the alert was sent'))
    # date when alert was created
    date_created = models.DateField(default=datetime.date.today,
        help_text=_('When the alert was created'))
    # draftlaws it refers to
    draftlaws = models.ManyToManyField(DraftLaw, related_name='sms_alerts',
        help_text=_('Draft Laws related to this alert'), blank=True)


    def __unicode__ (self):
        return u'%s' % self.text[:50]
