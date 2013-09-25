# -*- coding: utf-8 -*
"""
Views votingrecord
"""
__docformat__ = 'epytext en'

from django.views.generic import DetailView, ListView
try:
    from menus.utils import set_language_changer
except ImportError:
    from cms.utils import set_language_changer

from .models import VotingRecord, VotingRecordResult
from representative.models import Representative



class List (ListView):
    model = VotingRecord
    template_name = 'votingrecord/list.html'
    queryset = VotingRecord.objects.filter(name__isnull=False)
    paginate_by = 30



class Detail (DetailView):
    context_object_name = 'obj'
    model = VotingRecord
    template_name = 'votingrecord/detail.html'
    slug_field = 'slug'


    def get_context_data (self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        #read this in from user later
        session_number = 3
        context['counts'] = VotingRecordResult.get_counts(record=context['obj'], session=session_number)
        context['results'] = VotingRecordResult.objects.filter(record=context['obj'], session=session_number)

        order_by = VotingRecord._meta.ordering
        context['amended_by'] =\
            context['obj'].amended_by.all().order_by(*order_by)
        context['amending'] =\
            context['obj'].amending.all().order_by(*order_by)

        set_language_changer(self.request, context['obj'].get_absolute_url)
        return context
