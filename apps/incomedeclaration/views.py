# -*- coding: utf-8 -*-

"""
Views incomedeclaration
"""
__docformat__ = 'epytext en'

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
try:
    from menus.utils import set_language_changer
except ImportError:
    from cms.utils import set_language_changer

from .models import IncomeDeclaration



class List (ListView):
    model = IncomeDeclaration
    template_name = 'incomedeclaration/list.html'
    queryset = IncomeDeclaration.objects.all()
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context['url_feed'] = reverse('representative_feed_list')
        return context

class Detail (DetailView):
    context_object_name = 'obj'
    model = IncomeDeclaration
    template_name = 'incomedeclaration/detail.html'
    slug_field = 'slug'


    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        obj = context['obj']
        if obj.representative:
            context['url_feed'] = reverse('representative_feed_detail', args=[obj.representative.pk])
        else:
            context['url_feed'] = reverse('representative_feed_list')

        set_language_changer(self.request, obj.get_absolute_url)
        return context
