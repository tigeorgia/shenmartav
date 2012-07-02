"""
Admin question
"""
__docformat__ = 'epytext en'

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from .models import *


def make_public(modeladmin, request, queryset):
    for q in queryset:
        q.is_public = True
        q.save()
    #queryset.update(is_public=True) # doesn't call save()
make_public.short_description = _("Mark selected questions as public")


class QuestionAdmin (TranslationAdmin):
    list_display = ('is_public', 'date', 'question', 'representative', 'answer')
    list_display_links = ('is_public', 'question', 'answer')
    actions = [make_public]
    list_filter = ['is_public', 'date']
    date_hierarchy = 'date'
admin.site.register(Question, QuestionAdmin)
