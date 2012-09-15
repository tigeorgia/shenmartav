"""
Admin representative

Depends on popit.
"""
__docformat__ = 'epytext en'

from django.contrib import admin
from modeltranslation.admin import TranslationTabularInline, TranslationAdmin

from .models import Attendance, Term, Party, Unit, Representative,\
    AdditionalInformation, RandomRepresentative
from popit.admin import PositionInlineAdmin, PersonNameInlineAdmin, PersonAdmin,\
    OrganisationAdmin, OrgNameInlineAdmin
from popit.models import Person



class TermAdmin (TranslationAdmin):
    pass
admin.site.register(Term, TermAdmin)



class PartyAdmin (OrganisationAdmin):
    inlines = [
        OrgNameInlineAdmin,
    ]
    list_filter = ['unit']
admin.site.register(Party, PartyAdmin)



class UnitAdmin (TranslationAdmin):
    pass
admin.site.register(Unit, UnitAdmin)



class InlineAdditionalInformation (TranslationTabularInline):
    model = AdditionalInformation
    extra = 1

class InlineAttendanceAdmin (admin.TabularInline):
    model = Attendance
    extra = 1

class RepresentativeAdmin (PersonAdmin):
    inlines = [
        PersonNameInlineAdmin,
        PositionInlineAdmin,
        InlineAdditionalInformation,
        InlineAttendanceAdmin,
    ]
    list_filter = ['party', 'unit']
admin.site.register(Representative, RepresentativeAdmin)



class RandomRepresentativeAdmin (admin.ModelAdmin):
    pass
admin.site.register(RandomRepresentative, RandomRepresentativeAdmin)
