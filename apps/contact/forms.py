# -*- coding: utf-8 -*
"""
Forms for app contact
"""
__docformat__ = 'epytext en'

from django import forms
from django.utils.translation import ugettext_lazy as _



class ContactForm(forms.Form):
    first_name = forms.CharField(label=_('Your First Name'))
    last_name = forms.CharField(label=_('Your Last Name'), required=False)
    email = forms.EmailField(label=_('Your Email Address'), required=False)
    subject = forms.CharField(label=_('Subject'))
    body = forms.CharField(widget=forms.widgets.Textarea(), label=_('Body'))
