from modeltranslation.translator import translator, TranslationOptions

from apps.representative.models import Representative, AdditionalInformation, Unit, Cabinet, Faction, Term, Url, \
    FamilyIncome, Party

class RepresentativeTranslationOptions(TranslationOptions):
    fields = ('committee', 'electoral_district', 'elected',
              'pob', 'family_status', 'education', 'contact_address_phone',
              'expenses', 'property_assets',)


class AdditionalInformationTranslationOptions(TranslationOptions):
    fields = ('value',)


class UrlTranslationOptions(TranslationOptions):
    fields = ('label',)


class UnitTranslationOptions(TranslationOptions):
    fields = ('name',)


class CabinetTranslationOptions(TranslationOptions):
    fields = ('name',)


class FactionTranslationOptions(TranslationOptions):
    fields = ('name',)


class TermTranslationOptions(TranslationOptions):
    fields = ('name',)


class FamilyIncomeTranslationOptions(TranslationOptions):
    fields = ('fam_name', 'fam_role')


class PartyTranslationOptions(TranslationOptions):
    pass


translator.register(Representative, RepresentativeTranslationOptions)
translator.register(AdditionalInformation, AdditionalInformationTranslationOptions)
translator.register(Url, UrlTranslationOptions)
translator.register(Unit, UnitTranslationOptions)
translator.register(Cabinet, CabinetTranslationOptions)
translator.register(Faction, FactionTranslationOptions)
translator.register(Term, TermTranslationOptions)
translator.register(FamilyIncome, FamilyIncomeTranslationOptions)
translator.register(Party, PartyTranslationOptions)
