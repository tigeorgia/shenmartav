# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import get_language, ugettext_lazy as _

class SMSRegister (models.Model):
    """An user that registered for SMS alert."""

    # name of the registered user
    name = models.TextField(help_text=_('Your name'), blank=False)
    # language selected
    selected_language = models.TextField(help_text=_('Language to use'), blank=False)
    # phone number to send the SMS to.
    phone_number = models.TextField(help_text=_('Phone number to send the SMS to'), blank=False)
    # user email address
    email = models.EmailField(help_text=_('User email address'), blank=False)
    # groups the user chooses to subscribe to
    groups = models.TextField(help_text=_('Groups you are subscribing to'), blank=False)

    class Meta:
        ordering = ('-name',)


    def __unicode__ (self):
        return u'%s' % self.text[:50]

