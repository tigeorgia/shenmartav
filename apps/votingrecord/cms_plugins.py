from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import VotingRecord, VotingRecordPluginConf


NUM_RECORDS = 5


class VotingRecordPlugin (CMSPluginBase):
    model = VotingRecordPluginConf
    name = _('Voting Record Plugin')
    render_template = 'cmsplugins/votingrecord.html'

    def render(self, context, instance, placeholder):
        context['instance'] = instance

        records = VotingRecord.objects.all().filter(name__isnull=False)
        context['records'] = records[:NUM_RECORDS]

        return context

plugin_pool.register_plugin(VotingRecordPlugin)
