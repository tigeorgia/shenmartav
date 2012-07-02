"""
CMS Plugins draftlaw
"""
__docformat__ = 'epytext en'

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.db.models import Q
from django.utils.translation import get_language, ugettext_lazy as _

from .models import DraftLaw, DraftLawPluginConf, News, Alert



class DraftLawPlugin (CMSPluginBase):
    model = DraftLawPluginConf
    name = _('Draft Law Plugin')
    render_template = 'cmsplugins/draftlaw.html'


    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context
plugin_pool.register_plugin(DraftLawPlugin)
