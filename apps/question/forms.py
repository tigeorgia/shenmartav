# -*- coding: utf-8 -*
"""
Forms for app question

Depends on representative.
"""
__docformat__ = 'epytext en'

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Question
from representative.models import Representative



class QuestionForm (forms.ModelForm):
    email = forms.EmailField(label=_('Email Address'))

    class Meta:
        model = Question
        exclude = ('is_public', 'date',
            'first_name_en', 'first_name_ka',
            'last_name_en', 'last_name_ka',
            'question_en', 'question_ka',
            'answer', 'answer_en', 'answer_ka')


    def __init__ (self, **kwargs):
        if not 'initial' in kwargs and 'session' in kwargs:
            try:
                s = kwargs.pop('session')['form_question']
            except KeyError:
                pass
            else:
                initial = {}
                for item in ['representative', 'first_name', 'last_name',
                    'email', 'mobile']:
                    try:
                        initial[item] = s[item]
                    except KeyError:
                        pass
                if initial:
                    kwargs['initial'] = initial

        super(QuestionForm, self).__init__(**kwargs)
        self.fields['representative'].choices =\
            Representative.by_lastname_lastname_first(choices=True)
