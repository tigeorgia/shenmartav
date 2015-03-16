# -*- coding: utf-8 -*
"""
Forms for app smsregister
"""
__docformat__ = 'epytext en'

from django import forms
from django.utils.translation import ugettext_lazy as _
from apps.smsregister.models import SMSRegister
from captcha.fields import CaptchaField


class SMSRegisterForm(forms.Form):
    name = forms.CharField(label=_('Your Name: '), required=True)
    phone_number = forms.CharField(label=_('Mobile: +995'), required=True, max_length=9, min_length=9)
    email = forms.CharField(label=_('Email'), required=True, max_length=75, min_length=5)

    lang = forms.ChoiceField(label=_('Language'), required=True, 
        choices=(
            ('en', u"English"),
            ('ka', u"ქართული")),
        widget=forms.RadioSelect)
    
    only_important = False
    
    subscribe = forms.MultipleChoiceField(label=_('Subscribe to: '), 
        widget=forms.CheckboxSelectMultiple,
        required=True,
        choices=(
            (u"all",_(u"All")),
            (u"agriculture",_(u"Agrarian Issues Committee")),
            (u"budget",_(u"Budget and Finance Committee")),
            (u"environment",_(u"Committee on Environmental Protection and Natural Resources")),
            (u"diaspora",_(u"Diaspora and Caucasus Issues Committee")),
            (u"defence",_(u"Defence and Security Committee")),
            (u"education",_(u"Education, Science and Culture Committee")),
            (u"europe",_(u"European Integration Committee")),
            (u"foreignrelations",_(u"Foreign Relations Committee")),
            (u"healthcare",_(u"Healthcare and Social Issues Committee")),
            (u"humanrights",_(u"Human Rights and Civil Integration Committee")),
            (u"legalissues",_(u"Legal Issues Committee")),
            (u"rules",_(u"Procedural Issues and Rules Committee")),
            (u"regional",_(u"Regional Policy, Self-government and Mountainous Regions")),
            (u"economy",_(u"Sector Economy and Economic Policy Committee")),
            (u"sports",_(u"Sport and Youth Affairs Committee")),
            (u"adjara",_(u"Adjaran Supreme Council")),
            (u"debug",_(u"Debug")),
    ))

    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(SMSRegisterForm, self).__init__(*args, **kwargs)
        self.initial['lang'] = 'ka'

    def clean(self):
        cleaned_data = self.cleaned_data
        phone_number = cleaned_data.get('phone_number')

        if SMSRegister.objects.filter(phone_number=phone_number).exists():
            self._errors['phone_number'] = self.error_class([_('This phone number has already been registered.')])

        return cleaned_data


class SMSUnsubscribeForm(forms.Form):
    phone_number = forms.CharField(label=_('Mobile: +995'), required=True, max_length=9, min_length=9)
    only_important = False

    def __init__(self, *args, **kwargs):
        super(SMSUnsubscribeForm, self).__init__(*args, **kwargs)
