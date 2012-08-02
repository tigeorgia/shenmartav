"""
CMS Plugins draftlaw
"""
__docformat__ = 'epytext en'

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.db.models import Q
from django.utils.translation import get_language, ugettext_lazy as _

from .models import DraftLaw, DraftLawPluginConf, Alert
from basic.blog.models import Post



class DraftLawPlugin (CMSPluginBase):
    model = DraftLawPluginConf
    name = _('Draft Law Plugin')
    render_template = 'cmsplugins/draftlaw.html'


    def render(self, context, instance, placeholder):
        context['instance'] = instance
        try:
            context['post'] = Post.objects.published().order_by('-publish')[0]
        except IndexError:
            context['post'] = None
        return context
plugin_pool.register_plugin(DraftLawPlugin)
