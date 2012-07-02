from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from .models import RepresentativePluginConf, RandomRepresentative



class RepresentativePlugin (CMSPluginBase):
    model = RepresentativePluginConf
    name = _('Representative Plugin')
    render_template = 'cmsplugins/representative.html'


    def render(self, context, instance, placeholder):
        context['obj'] = RandomRepresentative.get()
        return context

plugin_pool.register_plugin(RepresentativePlugin)
