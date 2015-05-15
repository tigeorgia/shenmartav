# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class SMSRegisterApp (CMSApp):
    name = _('SMS Registration App')
    urls = ['smsregister.urls']
apphook_pool.register(SMSRegisterApp)
