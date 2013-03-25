from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from .models import SMSAlert

class SMSAlertPlugin (CMSPluginBase):
    model = CMSPlugin
    name = _('SMS Alert Plugin')
    render_template = 'smsalert/page.html'

    def render(self, context, instance, placeholder):
        context['obj'] = SMSAlert.objects.exclude().order_by('-date_sent').distinct()[0]
        return context

plugin_pool.register_plugin(SMSAlertPlugin)
