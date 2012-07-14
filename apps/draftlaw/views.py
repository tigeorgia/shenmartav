# -*- coding: utf-8 -*
"""
Views draftlaw
"""
__docformat__ = 'epytext en'

import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Max
from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView, ListView
try:
    from menus.utils import set_language_changer
except ImportError:
    from cms.utils import set_language_changer

from .models import DraftLaw, DraftLawDiscussion,\
    Alert as AlertModel



PAGINATE_BY = 30
NUM_STAGES = 6



class DraftLawForList (object):
    """Helper class to combine data from draft law and their discussions
    for List view.
    """
    def __init__ (self, item, updated, place=None):
        self.pk = item.pk
        self.title = item.title
        self.url = item.get_absolute_url()
        self.shortstatus = item.shortstatus

        self.updated = updated
        self.place = place

        self.stages = [{
            'css': 'missing',
            'info': '',
            } for i in xrange(NUM_STAGES)]

        max_stage = item.discussions.all().aggregate(Max('stage'))['stage__max']
        if max_stage is not None:
            for i in xrange(max_stage, NUM_STAGES):
                self.stages[i]['css'] = 'incomplete'

        for discussion in item.discussions.all():
            self.stages[discussion.stage]['css'] = 'complete'
             # append if several discussions on same stage
            self.stages[discussion.stage]['info'] +=\
                str(discussion.date) + ' :: ' + discussion.place + ' '




class Items (TemplateView):
    """Implements a view with paged draft law items."""
    template_name = 'draftlaw/items.html'


    def _get_page (self, page, queryset):
        """Get given queryset as page.

        @param page: page number to retrieve
        @type page: int
        @param queryset: queryset to paginate
        @type queryset: Django queryset
        @return: queryset as page
        @rtype: Paginator.page
        """
        paginator = Paginator(queryset, PAGINATE_BY)
        try:
            result = paginator.page(page)
        except (PageNotAnInteger, TypeError):
            result = paginator.page(1)
        except EmptyPage:
            result = None
        #    result = paginator.page(paginator.num_pages)

        return result


    def _combine_nondiscussed (self, parameters, discussions):
        """Combine given discussions with non-discussed draft laws.

        @param parameters: query parameters
        @type parameters: { 'page' : int, 'query': str }
        @param discussions: draft law discussions for this page
        @type discussions: [ draftlaw.DraftLawDiscussion ]
        @return: combined list of draft laws for list view
        @rtype: [ DraftLawForList ]
        """
        nondiscussed = DraftLaw.objects.filter(discussions__isnull=True)
        if 'query' in parameters:
            q = parameters['query']
            nondiscussed = nondiscussed.filter(
                Q(title__icontains=q) | Q(summary__icontains=q))

        combined = []
        discussions = list(discussions)
        if discussions:
            nondiscussed = nondiscussed.filter(
                bureau_date__gte=discussions[-1].date).filter(
                bureau_date__lt=discussions[0].date).order_by('-bureau_date')
            nondiscussed_idx = 0
            for d in discussions:
                try:
                    while 1:
                        nd = nondiscussed[nondiscussed_idx]
                        if nd.bureau_date > d.date:
                            combined.append(
                                DraftLawForList(nd, nd.bureau_date))
                            nondiscussed_idx += 1
                        else:
                            break
                except IndexError:
                    pass

                combined.append(DraftLawForList(d.draftlaw, d.date, d.place))
        else:
            for nd in nondiscussed.order_by('-bureau_date'):
                combined.append(DraftLawForList(nd, nd.bureau_date))

        return combined


    def _get_draftlaws (self, parameters):
        """Retrieve a list of draft laws.

        @param parameters: query parameters
        @type parameters: { 'page' : int, 'query': str }
        @return: page with draft laws (for list)
        @rtype: paginator.Page
        """
        qs = DraftLawDiscussion.objects.all()
        if 'query' in parameters:
            q = parameters['query']
            qs = qs.filter(Q(draftlaw__title__icontains=q) |\
                Q(draftlaw__summary__icontains=q) | Q(place__icontains=q))

        page = self._get_page(parameters['page'], qs.order_by('-date'))
        if page: # FIXME: no discussions -> no non-discussed
            page.object_list = self._combine_nondiscussed(
                parameters, page.object_list)
        return page


    def get_context_data (self, **kwargs):
        context = super(Items, self).get_context_data(**kwargs)
        context['draftlaws'] = self._get_draftlaws(context['params'])
        return context



class List (TemplateView):
    """Implements the draftlaw list view."""
    template_name = 'draftlaw/list.html'



class Detail (DetailView):
    """Implements the draftlaw detail view."""
    context_object_name = 'obj'
    model = DraftLaw
    template_name = 'draftlaw/detail.html'
    slug_field = 'slug'

    def get_context_data (self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        set_language_changer(self.request, context['obj'].get_absolute_url)
        return context



class Info (DetailView):
    context_object_name = 'obj'
    model = DraftLaw
    template_name = 'draftlaw/info.html'



class Alert (ListView):
    """Implements a view with one paged alert item."""
    template_name = 'draftlaw/alert.html'
    context_object_name = 'object_list'
    queryset = DraftLaw.objects.exclude(sms_ka__exact='',
        sms_en__exact='').order_by('-bureau_date').distinct()
    paginate_by = 1


    def get_context_data (self, **kwargs):
        context = super(Alert, self).get_context_data(**kwargs)
        context['alert'] = AlertModel(context['object_list'][0])
        return context



def query (request, query):
    data = []

    # search title and summary
    qtitle = Q(title__icontains=query)
    qsummary = Q(summary__icontains=query)
    for d in DraftLaw.objects.filter(qtitle | qsummary):
        data.append({'label': d.title, 'pk': d.pk})

    return HttpResponse(json.dumps(data), content_type='application/json')
