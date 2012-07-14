"""
Admin draftlaw
"""
__docformat__ = 'epytext en'

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import DraftLaw, DraftLawDiscussion, DraftLawChild



class InlineDiscussion (TranslationTabularInline):
    model = DraftLawDiscussion
class InlineChild (TranslationTabularInline):
    model = DraftLawChild



class DraftLawAdmin (TranslationAdmin):
    inlines = [
        InlineDiscussion,
        InlineChild
    ]
admin.site.register(DraftLaw, DraftLawAdmin)
