#*- coding: utf-8 -*
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

from apps.votingrecord.models import VotingRecordResult, VotingRecord
from question.forms import QuestionForm
from question.models import Question

from .models import Representative, RandomRepresentative, Party, Faction, Cabinet, Unit as UnitModel

from django.db import connection


class Find (TemplateView):
    """A view to implement the find page."""
    template_name='representative/find.html'

    def get_context_data (self, **kwargs):
        context = super(Find, self).get_context_data(**kwargs)
        context['url_search'] = reverse('representative_search')

        try:
            pk = self.request.session['representative']['find']['info_pk']
            context['obj'] = Representative.objects.get(pk=pk)
        except KeyError:
            context['obj'] = RandomRepresentative.get()

        unit = UnitModel.objects.get(short='parliament')
        reps = unit.active_term.representatives.all()
        factions = Faction.objects.filter(representatives__in=reps).distinct()
        cabinets = Cabinet.objects.filter(faction__in=factions).distinct()
        
        context['factions'] = factions
        context['cabinets'] = cabinets
        context['ushort'] = 'parliament'
        
        
        context['active_unit'] = context['obj'].unit.short
        context['url_feed'] = reverse('representative_feed_list')
        return context


class Search (TemplateView):
    """A view to implement the search page."""
    template_name = "representative/search.html"


    def get_queryset(self, query):
        return Representative.objects.filter(
            Q(slug__icontains=query) |
            Q(names__name__icontains=query) |
            Q(names__name_en__icontains=query) |
            Q(names__name_ka__icontains=query) |
            Q(names__title__icontains=query) |
            Q(names__title_en__icontains=query) |
            Q(names__title_ka__icontains=query) |
            Q(description__icontains=query) |
            Q(description_en__icontains=query) |
            Q(description_ka__icontains=query) |
            Q(party__names__name__icontains=query) |
            Q(party__names__name_en__icontains=query) |
            Q(party__names__name_ka__icontains=query) |
            Q(electoral_district__icontains=query) |
            Q(electoral_district_en__icontains=query) |
            Q(electoral_district_ka__icontains=query) |
            Q(elected__icontains=query) |
            Q(elected_en__icontains=query) |
            Q(elected_ka__icontains=query) |
            Q(pob__icontains=query) |
            Q(pob_en__icontains=query) |
            Q(pob_ka__icontains=query) |
            Q(family_status__icontains=query) |
            Q(family_status_en__icontains=query) |
            Q(family_status_ka__icontains=query) |
            Q(education__icontains=query) |
            Q(education_en__icontains=query) |
            Q(education_ka__icontains=query) |
            Q(salary__icontains=query) |
            Q(expenses__icontains=query) |
            Q(expenses_en__icontains=query) |
            Q(expenses_ka__icontains=query) |
            Q(property_assets__icontains=query) |
            Q(property_assets_en__icontains=query) |
            Q(property_assets_ka__icontains=query) |
            Q(committee__icontains=query) |
            Q(committee_en__icontains=query) |
            Q(committee_ka__icontains=query) |
            Q(faction__name__icontains=query) |
            Q(faction__name_en__icontains=query) |
            Q(faction__name_ka__icontains=query) |
            Q(additional_information__value__icontains=query) |
            Q(additional_information__value_en__icontains=query) |
            Q(additional_information__value_ka__icontains=query)
        ).distinct()


    def get_context_data (self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['url_find'] = reverse('representative_find')

        if 'query' in kwargs:
            context['representatives'] = []
            qs = self.get_queryset(kwargs['query'])
            for representative in qs:
                if representative.unit.active_term in representative.terms.all():
                    context['representatives'].append(representative)
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

        try:
            members = unit.active_term.representatives.all()
        except AttributeError:
            return []

        members = Representative.by_lastname_firstname_first(members)
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

    def _get_cabinets(self):
        """Get cabinets.

        @return: cabinets
        @rtype: [ representative.Cabinet ]
        """
        short = self.__class__.__name__.lower()[4:]
        try:
            cabinets = Cabinet.objects.distinct()
        except AttributeError:
            return []
            
        return cabinets
    
    def _get_factions(self):
        """Get factions in this unit.

        @return: parties in this unit
        @rtype: [ representative.Party ]
        """
        # UnitParliament -> parliament
        short = self.__class__.__name__.lower()[4:]
        try:
            unit = UnitModel.objects.get(short=short)
        except UnitModel.DoesNotExist:
            return []

        try:
            reps = unit.active_term.representatives.all()
            factions = Faction.objects.distinct().values('pk','name','short','cabinet__name')

        except AttributeError:
            return []
            
        return factions

    def get_context_data (self, **kwargs):
        context = super(Unit, self).get_context_data(**kwargs)
        context['cabinets'] = self._get_cabinets()
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



def unit_representative (request, pk):
    try:
        unit = Representative.objects.get(pk=pk).unit.short
    except Representative.DoesNotExist:
        unit = ''
    return HttpResponse(json.dumps(unit), content_type='application/json')



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
                'answered': { 'absolute': 0, 'relative': 50 },
                'noresponse': { 'absolute': 0, 'relative': 50 },
            }

        answered_absolute = len([p for p in public if p.answer])
        noresponse_absolute = total - answered_absolute

        if answered_absolute == noresponse_absolute: # might be all 0, too
            answered_relative = 50
            noresponse_relative = 50
        else:
            answered_relative = answered_absolute * 100. / total
            noresponse_relative = noresponse_absolute * 100. / total

        return {
            'last': public[0],
            'answered': {
                'absolute': answered_absolute,
                'relative': answered_relative
            },
            'noresponse': {
                'absolute': noresponse_absolute,
                'relative': noresponse_relative
            }
        }


    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        obj = context['obj']

        context['form'] = self._get_form(obj)
        context['questions'] = self._get_questions(obj)
        totalCount = VotingRecordResult.get_counts(representative=obj)

        context['attended'] = totalCount['total'] - totalCount['absent']
        context['absent'] = totalCount['absent']
        if totalCount['total'] == 0:
            context['percentage_attended'] = 0
            context['percentage_absent'] = 0
            context['percentage_attended_string'] = "N/A"
        else:
            context['percentage_attended'] = context['attended'] / float(totalCount['total']) * 100
            context['percentage_absent'] = 100 - context['percentage_attended']
            context['percentage_attended_string'] = "{0:.2f}".format(context['percentage_attended'])

        #votecountall = VotingRecordResult.get_counts(representative=obj)
        #context['votecounts'] = votecountall
        context['votecounts'] = VotingRecordResult.get_counts(representative=obj,session=3)
        context['lawvotecounts'] = VotingRecordResult.get_counts(representative=obj,lawcount=True)
                        
        context['url_feed'] = reverse('representative_feed_detail', args=[obj.pk])
        context['url_votingrecords'] = reverse(
            'representative_votingrecords', args=[obj.pk, obj.slug])
        try:
            context['decl'] = obj.incomedeclaration.all()[0]
        except IndexError:
            context['decl'] = None
        
            
        try:
            context['faminc'] = obj.family_income.all().order_by('-submission_date')[0]
        except IndexError:
            context['faminc'] = None
            
        try:
            names_to_exclude = ["Facebook","Twitter","LinkedIn","Wikipedia","Asset Link"] 
            context['mainlinks'] = obj.urls.all().exclude(label__in=names_to_exclude)
        except IndexError:
            context['mainlinks'] = None
            
        try:
            context['sociallinks'] = obj.urls.all().exclude(label__icontains="მთავარი")
        except IndexError:
            context['sociallinks'] = None
        
        set_language_changer(self.request, obj.get_absolute_url)
        return context


def _get_votingrecord_results (representative):
    """Get voting record results for given representative

    @param representative: representative to get voting record results for
    @type representative: representative.Representative
    @return: list of dicts with voting record results
    @rtype: [{'css', 'vote', 'record', 'url', 'record__name'}]
    """
    results = representative.votingresults.filter(session=3).values(
        'css', 'vote', 'record','record__name','record__date').order_by('-record__date')
    for r in results:
        r['url'] = reverse('votingrecord_detail', args=[r['record']])

    return results


class VotingRecordsSimple (DetailView):
    """Simple view to return voting records HTML for AJAX requests."""
    context_object_name = 'obj'
    model = Representative
    template_name = 'representative/votingrecords_simple.html'

    def get_context_data(self, **kwargs):
        context = super(VotingRecordsSimple, self).get_context_data(**kwargs)
        context['results'] = _get_votingrecord_results(context['obj'])

        return context



class VotingRecords (DetailView):
    """Full view to return voting records HTML for a page."""
    context_object_name = 'obj'
    model = Representative
    template_name = 'representative/votingrecords.html'

    def get_context_data(self, **kwargs):
        context = super(VotingRecords, self).get_context_data(**kwargs)
        set_language_changer(self.request, context['obj'].get_absolute_url)
        context['results'] = _get_votingrecord_results(context['obj'])

        return context



class Info (Detail):
    context_object_name = 'obj'
    model = Representative
    template_name = 'representative/info.html'

    def _set_session (self, context):
        # use previously shown representative
        session = self.request.session
        if 'representative' not in session:
            session['representative'] = {}
        if 'find' not in session['representative']:
            session['representative']['find'] = {}
        session['representative']['find']['info_pk'] = context['obj'].pk
        session.modified = True


    def get_context_data(self, **kwargs):
        context = super(Info, self).get_context_data(**kwargs)
        self._set_session(context)
        return context



def query (request, query):
    data = []

    # search names & electoral districts
    for representative in Representative.objects.filter(
        Q(names__name__icontains=query) |
        Q(names__name_en__icontains=query) |
        Q(names__name_ka__icontains=query) |
        Q(electoral_district__icontains=query) |
        Q(electoral_district_en__icontains=query) |
        Q(electoral_district_ka__icontains=query)
    ):
        if representative.unit.active_term in representative.terms.all():
            data.append({
                'label': str(representative.name),
                'pk': representative.pk,
            })

    return HttpResponse(json.dumps(data), content_type='application/json')
