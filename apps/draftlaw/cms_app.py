# -*- coding: utf-8 -*-

"""
CMS App draftlaw
"""
__docformat__ = 'epytext en'

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _



class DraftLawApp (CMSApp):
    name = _('DraftLaw App')
    urls = ['draftlaw.urls']
apphook_pool.register(DraftLawApp)
