"""
Admin votingrecord
"""
__docformat__ = 'epytext en'

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import VotingRecord, VotingRecordAmendment, VotingRecordResult

class InlineAmendment (admin.TabularInline):
    model = VotingRecordAmendment
class InlineResult (admin.TabularInline):
    model = VotingRecordResult


class VotingRecordAdmin (TranslationAdmin):
    list_display = ('number', 'kan_id', 'name',)
    ordering = ['number']
    inlines = [
        InlineAmendment,
        InlineResult,
    ]
admin.site.register(VotingRecord, VotingRecordAdmin)
