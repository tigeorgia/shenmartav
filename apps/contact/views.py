# -*- coding: utf-8 -*
"""
Views contact
"""
__docformat__ = 'epytext en'


from django.core.mail import mail_managers
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views.generic import FormView, TemplateView

from .forms import ContactForm



class Show (FormView):
    """Show contact form."""
    template_name = 'contact/show.html'
    form_class = ContactForm


    def form_valid (self, form):
        subject = '[' + _('Contact Form') + '] ' + form.data['subject']
        body = form.data['first_name'] + ' ' + form.data['last_name'] + ':\n' +\
            form.data['email'] + '\n\n' +\
            form.data['body']
        mail_managers(subject, body)

        return redirect('contact_thanks')


    def form_invalid (self, form):
        return self.render_to_response({'form': form})



class Thanks (TemplateView):
    """Show thanks page."""
    template_name = 'contact/thanks.html'
