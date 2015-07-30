# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ContactApp (CMSApp):
    name = _('Contact App')
    urls = ['apps.contact.urls']
apphook_pool.register(ContactApp)
