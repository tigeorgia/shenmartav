# -*- coding: utf-8 -*
"""
Views draftlaw
"""
__docformat__ = 'epytext en'

from django.views.generic import TemplateView

from .models import SMSAlert



class Page (TemplateView):
    """Implements a view with one paged SMSAlert item."""
    template_name = 'smsalert/page.html'
