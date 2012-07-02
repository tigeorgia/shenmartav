from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import get_language, ugettext_lazy as _

from .models import Question, QuestionPluginConf
from .forms import QuestionForm
from representative.models import Representative, RandomRepresentative


class QuestionPlugin (CMSPluginBase):
    model = QuestionPluginConf
    name = _('Question Plugin')
    render_template = 'cmsplugins/question.html'

    def render(self, context, instance, placeholder):
        answered = Question.public.filter(answer__isnull=False)
        try:
            latest = answered.order_by('-date')[0]
        except IndexError:
            latest = None
        context['latest'] = latest

        representatives = Representative.objects.all()
        try:
            context['most_active'] = representatives.order_by('-answered')[0]
        except IndexError:
            context['most_active'] = None
        try:
            context['least_active'] = representatives.order_by('answered')[0]
        except IndexError:
            context['least_active'] = None

        context['representatives'] = representatives
        context['random'] = RandomRepresentative.get()

        return context

plugin_pool.register_plugin(QuestionPlugin)
