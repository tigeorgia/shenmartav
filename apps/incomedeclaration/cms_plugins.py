from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import IncomeDeclaration, IncomeDeclarationPluginConf


NUM_RECORDS = 5


class IncomeDeclarationPlugin (CMSPluginBase):
    model = IncomeDeclarationPluginConf
    name = _('Income Declaration Plugin')
    render_template = 'cmsplugins/incomedeclaration.html'

    def render(self, context, instance, placeholder):
        context['instance'] = instance

        obj_list = IncomeDeclaration.objects.all()
        context['obj_list'] = obj_list[:NUM_RECORDS]

        return context

plugin_pool.register_plugin(IncomeDeclarationPlugin)
