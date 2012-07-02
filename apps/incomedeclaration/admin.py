"""
Admin incomedeclaration
"""
__docformat__ = 'epytext en'

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import *

class InlineSecurity (TranslationTabularInline):
    model = DeclarationSecurity
class InlineFamily (TranslationTabularInline):
    model = DeclarationFamily
class InlineContract (TranslationTabularInline):
    model = DeclarationContract
class InlineDeposit (TranslationTabularInline):
    model = DeclarationDeposit
class InlineCash (TranslationTabularInline):
    model = DeclarationCash
class InlineGift (TranslationTabularInline):
    model = DeclarationGift
class InlineEntrepreneurial (TranslationTabularInline):
    model = DeclarationEntrepreneurial
class InlineRealEstate (TranslationTabularInline):
    model = DeclarationRealEstate
class InlineWage (TranslationTabularInline):
    model = DeclarationWage
class InlineProperty (TranslationTabularInline):
    model = DeclarationProperty
class InlineOtherInclExpense (TranslationTabularInline):
    model = DeclarationOtherInclExpense
class InlineBiography (TranslationTabularInline):
    model = DeclarationBiography

class IncomeDeclarationAdmin (TranslationAdmin):
    inlines = [
        InlineBiography,
        InlineFamily,
        InlineContract,
        InlineDeposit,
        InlineCash,
        InlineGift,
        InlineEntrepreneurial,
        InlineRealEstate,
        InlineWage,
        InlineProperty,
        InlineSecurity,
        InlineOtherInclExpense,
    ]

admin.site.register(IncomeDeclaration, IncomeDeclarationAdmin)

