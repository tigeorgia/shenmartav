# -*- coding: utf-8 -*-

"""
Admin draftlaw
"""
__docformat__ = 'epytext en'

from django.contrib import admin
from django.db import models
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import DraftLaw, DraftLawDiscussion, DraftLawChild
from tinymce.widgets import TinyMCE


class InlineDiscussion(TranslationTabularInline):
    model = DraftLawDiscussion


class InlineChild(TranslationTabularInline):
    model = DraftLawChild


class DraftLawAdmin(TranslationAdmin):
    list_display = ['bill_number', 'bureau_date', 'title']
    search_fields = ['bureau_date']
    sort_fields = ['bureau_date']

    inlines = [
        InlineDiscussion,
        InlineChild
    ]


admin.site.register(DraftLaw, DraftLawAdmin)
