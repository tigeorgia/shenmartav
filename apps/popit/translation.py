from modeltranslation.translator import translator, TranslationOptions
from apps.popit.models import Person, PersonName, Organisation, OrganisationName, Position


class PersonTranslationOptions(TranslationOptions):
    fields = ('description',)


class PersonNameTranslationOptions(TranslationOptions):
    fields = ('title', 'name',)


class OrganisationTranslationOptions(TranslationOptions):
    fields = ('summary',)


class OrganisationNameTranslationOptions(TranslationOptions):
    fields = ('name',)


class PositionTranslationOptions(TranslationOptions):
    fields = ('title', 'place', 'note',)


translator.register(Person, PersonTranslationOptions)
translator.register(PersonName, PersonNameTranslationOptions)
translator.register(Organisation, OrganisationTranslationOptions)
translator.register(OrganisationName, OrganisationNameTranslationOptions)
translator.register(Position, PositionTranslationOptions)
