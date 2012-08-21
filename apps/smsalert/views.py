# -*- coding: utf-8 -*
"""
Views draftlaw
"""
__docformat__ = 'epytext en'

from django.views.generic import ListView

from .models import SMSAlert



class Page (ListView):
    """Implements a view with one paged SMSAlert item."""
    template_name = 'smsalert/page.html'
    context_object_name = 'object_list'
    queryset = SMSAlert.objects.exclude().order_by('-date_sent').distinct()
    paginate_by = 1


    def get_context_data (self, **kwargs):
        context = super(Page, self).get_context_data(**kwargs)
        try:
            context['obj'] = context['object_list'][0]
        except IndexError:
            context['obj'] = None
        return context
