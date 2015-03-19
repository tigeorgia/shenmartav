# -*- coding: utf-8 -*
"""
Views contact
"""
__docformat__ = 'epytext en'


from django.core.mail import send_mail
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views.generic import FormView, TemplateView
from apps.smsregister.models import SMSRegister
from django.contrib import messages

from .forms import SMSRegisterForm, SMSUnsubscribeForm



class Show (FormView):
    """Show SMS registration form."""
    template_name = 'smsregister/show.html'
    form_class = SMSRegisterForm


    def form_valid (self, form):
        SEP = u"|"
        subject = u""

        user_name = form.cleaned_data['name']
        phone_number = form.cleaned_data['phone_number']
        language = form.cleaned_data['lang']
        groups = form.cleaned_data['subscribe']
        email = form.cleaned_data['email']

        body = (u"addmobile " + 
                user_name.replace(u" ",u"") + SEP +
                u"+995" + phone_number + SEP +
                language + SEP +
                u"False" + SEP +
                u','.join(groups))

        send_mail(subject, body, 'registration@myparliament.ge',['george.topouria@transparency.ge'])

        new_user = SMSRegister(name=user_name, selected_language=language,
                               phone_number=phone_number, email=email, groups=u'|'.join(groups).upper())
        new_user.save()

        return redirect('smsregister_thanks')


    def form_invalid (self, form):
        return self.render_to_response({'form': form})


class Unsubscribe (FormView):
    """Show unsubscription page."""
    template_name = 'smsregister/unsubscribe.html'
    form_class = SMSUnsubscribeForm

    def form_valid (self, form):

        phone_number = form.cleaned_data['phone_number']

        try:
            user_to_delete = SMSRegister.objects.get(phone_number=phone_number)
        except SMSRegister.DoesNotExist:
            return self.render_to_response({'form': form, 'error_message': _('This phone number you entered is not registered')})

        if user_to_delete:
            user_to_delete.delete()
            return redirect('smsregister_thanks')
        else:
            return self.render_to_response({'form': form, 'error_message': _('This phone number you entered is not registered')})


    def form_invalid (self, form):
        return self.render_to_response({'form': form, 'error_message': _('This phone number you entered is not registered')})


class Thanks (TemplateView):
    """Show thanks page."""
    template_name = 'smsregister/thanks.html'




