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


    def _add_activity (self, representative):
        representative.unanswered = {
            'absolute': Question.public.filter(
                representative=representative, answer__isnull=True).count(),
            'relative': 100 - representative.answered
        }
        representative.answered = {
            'absolute': Question.public.filter(
                representative=representative, answer__isnull=False).count(),
            'relative': representative.answered
        }

        return representative


    def render(self, context, instance, placeholder):
        answered = Question.public.filter(answer__isnull=False)
        try:
            latest = answered.order_by('-date')[0]
        except IndexError:
            latest = None
        context['latest'] = latest

        representatives = Representative.objects.all()
        try:
            representative = representatives.order_by('-answered')[0]
            context['most_active'] = self._add_activity(representative)
        except IndexError:
            context['most_active'] = None

        try:
            representative = representatives.order_by('answered')[0]
            context['least_active'] = self._add_activity(representative)
        except IndexError:
            context['least_active'] = None

        context['representatives'] = representatives
        context['random'] = RandomRepresentative.get()

        return context

plugin_pool.register_plugin(QuestionPlugin)
