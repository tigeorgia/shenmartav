from modeltranslation.translator import translator, TranslationOptions

from apps.smsalert.models import SMSAlert


class SMSAlertTranslationOptions(TranslationOptions):
    fields = ('text',)


translator.register(SMSAlert, SMSAlertTranslationOptions)
