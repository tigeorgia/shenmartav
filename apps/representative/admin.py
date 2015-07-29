# -*- coding: utf-8 -*-

"""
Admin representative

Depends on popit.
"""
__docformat__ = 'epytext en'

from django.contrib import admin
from django.db import models

from modeltranslation.admin import TranslationTabularInline, TranslationAdmin

from .models import Attendance, Term, Party, Cabinet, Faction, Unit, Representative, \
    AdditionalInformation, Url, RandomRepresentative
from apps.popit.admin import PositionInlineAdmin, PersonNameInlineAdmin, PersonAdmin, \
    OrganisationAdmin, OrgNameInlineAdmin
from apps.popit.models import Person

from tinymce.widgets import TinyMCE


class TermAdmin(TranslationAdmin):
    search_fields = ['name_en', 'name_ka']


admin.site.register(Term, TermAdmin)


class PartyAdmin(OrganisationAdmin):
    inlines = [
        OrgNameInlineAdmin,
    ]
    list_filter = ['unit']
    search_fields = ['slug', 'names__name_en', 'names__name_ka']


admin.site.register(Party, PartyAdmin)


class FactionAdmin(TranslationAdmin):
    search_fields = ['name_en', 'name_ka']


admin.site.register(Faction, FactionAdmin)


class CabinetAdmin(TranslationAdmin):
    list_display = ['name', 'position']
    list_editable = ['position']
    search_fields = ['name_en', 'name_ka', 'position']


admin.site.register(Cabinet, CabinetAdmin)


class UnitAdmin(TranslationAdmin):
    search_fields = ['name_en', 'name_ka', 'short']


admin.site.register(Unit, UnitAdmin)


class InlineAdditionalInformation(TranslationTabularInline):
    model = AdditionalInformation
    extra = 1


class InlineUrl(TranslationTabularInline):
    model = Url
    extra = 1


class InlineAttendanceAdmin(admin.TabularInline):
    model = Attendance
    extra = 1


class RepresentativeAdmin(PersonAdmin):
    inlines = [
        PersonNameInlineAdmin,
        PositionInlineAdmin,
        InlineAdditionalInformation,
        InlineUrl,
        InlineAttendanceAdmin,
    ]
    list_filter = ['party', 'unit']
    search_fields = ['slug', 'names__name_en', 'names__name_ka', 'date_of_birth']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
    }


admin.site.register(Representative, RepresentativeAdmin)


class RandomRepresentativeAdmin(admin.ModelAdmin):
    pass


admin.site.register(RandomRepresentative, RandomRepresentativeAdmin)
