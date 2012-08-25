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
        questions = Question.public.filter(representative=representative).count()
        answered = Question.answered.filter(representative=representative).count()
        representative.unanswered = {
            'absolute': questions - answered,
            'relative': 100 - representative.answered
        }
        representative.answered = {
            'absolute': answered,
            'relative': representative.answered
        }

        return representative


    def render(self, context, instance, placeholder):
        representatives = Representative.parliament.all()
        context['representatives'] = Representative.by_lastname_lastname_first(
            representatives=representatives)
        context['random'] = RandomRepresentative.get()

        try:
            latest = Question.answered.order_by('-date')[0]
        except IndexError:
            latest = None
        context['latest'] = latest

        if not latest:
            context['most_active'] = None
            context['least_active'] = None
            return context

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

        return context

plugin_pool.register_plugin(QuestionPlugin)
