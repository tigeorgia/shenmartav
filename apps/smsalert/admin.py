"""
Admin smsalert
"""
__docformat__ = 'epytext en'

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import SMSAlert



class SMSAlertAdmin (TranslationAdmin):
    pass
admin.site.register(SMSAlert, SMSAlertAdmin)
