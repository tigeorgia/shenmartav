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
from apps.representative.models import Representative


class List(ListView):
    model = VotingRecord
    template_name = 'votingrecord/list.html'

    queryset = VotingRecord.objects.filter(name__isnull=False)
    paginate_by = 30


class Detail(DetailView):
    context_object_name = 'obj'
    model = VotingRecord
    template_name = 'votingrecord/detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        context['counts1'] = VotingRecordResult.get_counts(record=context['obj'], session=1)
        context['votes1'] = VotingRecordResult.objects.filter(record=context['obj'], session=1)
        context['counts2'] = VotingRecordResult.get_counts(record=context['obj'], session=2)
        context['votes2'] = VotingRecordResult.objects.filter(record=context['obj'], session=2)
        context['counts3'] = VotingRecordResult.get_counts(record=context['obj'], session=3)
        context['votes3'] = VotingRecordResult.objects.filter(record=context['obj'], session=3)

        order_by = VotingRecord._meta.ordering
        context['amended_by'] = \
            context['obj'].amended_by.all().order_by(*order_by)
        context['amending'] = \
            context['obj'].amending.all().order_by(*order_by)

        set_language_changer(self.request, context['obj'].get_absolute_url)
        return context
