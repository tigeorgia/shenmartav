# -*- coding: utf-8 -*
"""
Views question

Depends on representative.
"""
__docformat__ = 'epytext en'

import datetime, socket

from django.contrib.sites.models import Site
from django.core.mail import mail_managers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views.generic import DetailView, ListView, FormView, TemplateView
try:
    from menus.utils import set_language_changer
except ImportError:
    from cms.utils import set_language_changer

try:
    from settings import QUESTION_SMS_EMAIL
except ImportError:
    QUESTION_SMS_EMAIL = 'root@localhost'

from representative.models import Representative

from .models import Question
from .forms import QuestionForm


#: pagination value
PAGINATE_BY = 30

def _get_form (view, representative=None):
    """Get question form for given representative.

    @param view: view object
    @type view: generic view
    @param representative: representative to get form for
    @type representative: representative.Representative
    @return: question form for given representative
    @type: QuestionForm
    """
    if representative:
        if 'form_question' in view.request.session:
            view.request.session['form_question']['representative'] =\
                representative.pk
        else:
            view.request.session['form_question'] = {
                'representative': representative.pk
            }

    return QuestionForm(session=view.request.session)



def notify_question_change (pk, question):
    """Notify site managers of a new/changed question.

    @param pk: primary key of the question
    @type pk: int
    @param question: question being asked
    @type question: str
    """
    subject = _('New question: %d') % pk

    uri = reverse('admin:question_question_change', args=(pk,))
    if uri.startswith('/mapit'): # err... FIXME?
        uri = uri[6:]
    site = Site.objects.get_current()
    message = _('%(question)s\n\nPlease manage at http://%(domain)s%(uri)s' % {
        'question': question,
        'domain': site.domain,
        'uri': uri}
    )

    try:
        mail_managers(subject, message)
    except socket.error: # silently ignore if mail system not setup, e.g. localhost
        pass


class List (ListView):
    """Implements the Question list view."""
    template_name = 'question/list.html'
    model = Question
    queryset = Question.public.order_by('-date')


    def get_context_data (self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context['form'] = _get_form(self)
        context['url_feed'] = reverse('question_feed_list')
        return context



class Ask (FormView):
    """Implements the Question ask view."""
    template_name = 'question/ask.html'
    form_class = QuestionForm
 
 
    def form_valid (self, form):
        obj = form.save()
 
        # at some stage it might be wise to have these added to a queueing
        # system (celery? rabbitmq?)
        notify_question_change(obj.pk, obj.question)
 
        self.request.session['form_question'] = {
            'representative': obj.representative.pk,
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'email': obj.email,
            'mobile': obj.mobile,
        }
 
        return redirect('question_thanks')
 
 
    def form_invalid (self, form):
        return self.render_to_response({'form': form})
 
 
    def get_context_data (self, **kwargs):
        context = super(Ask, self).get_context_data(**kwargs)
 
        if 'pk' in self.kwargs: # from query params
            if 'form_question' in self.request.session:
                self.request.session['form_question']['representative'] =\
                    self.kwargs['pk']
            else:
                self.request.session['form_question'] = {
                    'representative': self.kwargs['pk']
                }
 
        question = context['form'].instance
        context['form'] = QuestionForm(instance=question,
            session=self.request.session)
        context['url_feed'] = reverse('question_feed_list')
 
        return context



class Thanks (TemplateView):
    """Implements the Question thanks view."""
    template_name = 'question/thanks.html'

    def get_context_data (self, **kwargs):
        context = super(Thanks, self).get_context_data(**kwargs)

        if 'form_question' in self.request.session:
            context['representative'] =\
                self.request.session['form_question']['representative']
        context['url_feed'] = reverse('question_feed_list')

        return context


class Detail (DetailView):
    """Implements the Question detail view."""
    context_object_name = 'obj'
    model = Question
    queryset = Question.public
    slug_field = 'pk'
    template_name = 'question/detail.html'


    def get_context_data (self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        context['form'] = _get_form(self, context['obj'].representative)
        context['url_feed'] = reverse('question_feed_list')
        set_language_changer(self.request, context['obj'].get_absolute_url)

        return context



class Leaderboard (ListView):
    """Shows a leaderboard of representatives by questions answered."""
    model = Representative
    queryset = Representative.objects.filter(questions__is_public=True,
        questions__isnull=False).distinct().order_by('-answered')
    template_name = 'question/leaderboard.html'


    def get_context_data (self, **kwargs):
        context = super(Leaderboard, self).get_context_data(**kwargs)
        context['url_feed'] = reverse('question_feed_list')
        return context



class Info (DetailView):
    context_object_name = 'obj'
    model = Question
    queryset = Question.public
    template_name = 'question/info.html'


    def get_context_data (self, **kwargs):
        context = super(Info, self).get_context_data(**kwargs)
        return context



class Items (TemplateView):
    """Implements a view with paged question items."""
    template_name = 'question/items.html'


    def _add_item_states (self, page):
        """Set item states in given page.

        @param page: page number to retrieve
        @type page: int
        @return: a page with questions
        @rtype: Paginator.page
        """
        if not page:
            return None

        two_weeks_ago = datetime.date.today() - datetime.timedelta(14)
        answered = { 'text': 'answered', 'value': 2 }
        unanswered_new = { 'text': 'unanswered-new', 'value': 1 }
        unanswered_old = { 'text': 'unanswered-old', 'value': 0 }

        for item in page.object_list:
            if item.answer:
                item.state = answered
            else:
                if item.date >= two_weeks_ago:
                    item.state = unanswered_new
                else:
                    item.state = unanswered_old

        return page


    def _get_items (self, page):
        """Get given queryset as page.

        @param page: page number to retrieve
        @type page: int
        @return: a page with questions
        @rtype: Paginator.page
        """
        queryset = Question.public.order_by('-date')
        paginator = Paginator(queryset, PAGINATE_BY)
        try:
            result = paginator.page(page)
        except (PageNotAnInteger, TypeError):
            result = paginator.page(1)
        except EmptyPage:
            result = None
        #    result = paginator.page(paginator.num_pages)

        return self._add_item_states(result)


    def get_context_data (self, **kwargs):
        context = super(Items, self).get_context_data(**kwargs)
        context['items'] = self._get_items(context['params']['page'])
        return context



def receive (request, mobile, representative, question):
    """Receive questions from sms server.

    @param mobile: mobile phone number of the asker
    @type mobile: str
    @param representative: id of the representative to ask
    @type representative: int
    @param question: question asked
    @type question: str
    @return: response, either 'Bad data' or 'OK'
    @rtype: HttpResponse
    """
    try:
        question = Question(representative_id=representative,
            name=_('SMS'), email=QUESTION_SMS_EMAIL, mobile=mobile, question=question,
        )
        question.save()
    except (ValueError, IntegrityError):
        return HttpResponseBadRequest('Bad data')

    notify_question_change(question.pk, question.question)
    return HttpResponse('OK')
