# -*- coding: utf-8 -*
"""
Views for Representative app

Depends on question and votingrecord.
"""
__docformat__ = 'epytext en'

import json
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, TemplateView, ListView
try:
    from menus.utils import set_language_changer
except ImportError:
    from cms.utils import set_language_changer

from votingrecord.models import VotingRecordResult
from question.forms import QuestionForm
from question.models import Question

from .models import Representative, RandomRepresentative, Party, Unit as UnitModel



class Find (TemplateView):
    """A view to implement the find page."""
    template_name='representative/find.html'

    def get_context_data (self, **kwargs):
        context = super(Find, self).get_context_data(**kwargs)
        context['url_search'] = reverse('representative_search')
        context['obj'] = RandomRepresentative.get()
        context['units'] = UnitModel.objects.all()
        context['url_feed'] = reverse('representative_feed_list')
        return context



class Search (TemplateView):
    """A view to implement the search page."""
    template_name = "representative/search.html"


    def get_queryset(self, query):
        return Representative.objects.filter(
            Q(slug__icontains=query) |
            Q(names__name__icontains=query) |
            Q(names__title__icontains=query) |
            Q(description__icontains=query) |
            Q(party__names__name__icontains=query) |
            Q(electoral_district__icontains=query) |
            Q(elected__icontains=query) |
            Q(pob__icontains=query) |
            Q(family_status__icontains=query) |
            Q(education__icontains=query) |
            Q(attendance_record__icontains=query) |
            Q(salary__icontains=query) |
            Q(expenses__icontains=query) |
            Q(property_assets__icontains=query) |
            Q(committee__icontains=query) |
            Q(faction__icontains=query) |
            Q(additional_information__value__icontains=query)
        ).distinct()


    def get_context_data (self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['url_find'] = reverse('representative_find')

        if 'query' in kwargs:
            context['representatives'] = self.get_queryset(kwargs['query'])
            context['query'] = kwargs['query']

        context['url_feed'] = reverse('representative_feed_list')
        return context


    def post (self, request, **kwargs):
        kwargs['query'] = request.POST.get('query')
        return self.render_to_response(self.get_context_data(**kwargs))




class Unit (TemplateView):
    """A base view to implement a political unit."""
    template_name='representative/unit.html'

    def _get_members (self):
        """Get members of this unit.

        @return: members of this unit
        @rtype: [ representative.Representative ]
        """
        # UnitParliament -> parliament
        short = self.__class__.__name__.lower()[4:]
        try:
            unit = UnitModel.objects.get(short=short)
        except UnitModel.DoesNotExist:
            return []

        members = Representative.by_lastname_firstname_first(
            Representative.objects.filter(unit=unit))

        for member in members:
            """
            Avoid a browser bug with names longer than available width making
            member boxes in the unit of the find page jump up a few pixels.
            You probably need to apply the template tag filter 'linebreaksbr' when
            using this.
            Note the replacement only done once - the box starts jumping again
            if there are three parts seperated by the linebreak *sigh*
            """
            member['name'] = member['firstname_first'].replace(' ', '\n', 1)
        return members


    def get_context_data (self, **kwargs):
        context = super(Unit, self).get_context_data(**kwargs)
        context['members'] = self._get_members()
        return context



class UnitParliament (Unit):
    """A view to implement the unit Parliament of Georgia."""
    template_name='representative/unit.html'
class UnitAjara (Unit):
    """A view to implement the unit Ajara Supreme Council."""
    template_name='representative/unit.html'
class UnitTbilisi (Unit):
    """A view to implement the unit Tbilisi City Council."""
    template_name='representative/unit.html'



class Detail (DetailView):
    context_object_name = 'obj'
    model = Representative
    template_name = 'representative/detail.html'


    def _get_form (self, obj):
        """Get question form for this representative.

        @param obj: this representative
        @type obj: representative.Representative
        @return: question form
        @rtype: forms.QuestionForm
        """
        if 'form_question' in self.request.session:
            self.request.session['form_question']['representative'] =\
                obj.pk
        else:
            self.request.session['form_question'] = {
                'representative': obj.pk
            }
        return QuestionForm(session=self.request.session)


    def _get_questions (self, obj):
        """Get questions for this representative.

        @param obj: this representative
        @type obj: representative.Representative
        @return: questions
        @rtype: {
            'last' : question.Question,
            'answered': {'absolute': int, 'relative': int }
            'noresponse': {'absolute': int, 'relative': int }
        }
        """
        # can't seem to do it via managers in related objects
        public = [
            q for q in obj.questions.all().order_by('-date') if q.is_public
        ]
        total = len(public)
        if total == 0:
            return {
                'last': [],
                'answered': { 'absolute': 0, 'relative': 0 },
                'noresponse': { 'absolute': 0, 'relative': 0 },
            }

        answered = len([p for p in public if p.answer])
        noresponse = total - answered
        return {
            'last': public[0],
            'answered': {
                'absolute': answered,
                'relative': answered * 100. / total
            },
            'noresponse': {
                'absolute': noresponse,
                'relative': noresponse * 100. / total
            }
        }


    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        obj = context['obj']

        context['form'] = self._get_form(obj)
        context['questions'] = self._get_questions(obj)
        context['votecounts'] = VotingRecordResult.get_counts(representative=obj)
        context['url_feed'] = reverse('representative_feed_detail', args=[obj.pk])

        set_language_changer(self.request, obj.get_absolute_url)
        return context



class VotingRecords (DetailView):
    context_object_name = 'obj'
    model = Representative
    template_name = 'representative/votingrecords.html'



class Info (DetailView):
    context_object_name = 'obj'
    model = Representative
    template_name = 'representative/info.html'

    def get_context_data(self, **kwargs):
        context = super(Info, self).get_context_data(**kwargs)
        return context



def query (request, query):
    data = []

    # search names & electoral districts
    for r in Representative.objects.filter(
        Q(names__name__icontains=query) |\
        Q(electoral_district__icontains=query)):
        data.append({'label': str(r.name), 'pk': r.pk})

    return HttpResponse(json.dumps(data), content_type='application/json')
