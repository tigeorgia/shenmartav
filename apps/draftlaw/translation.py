from modeltranslation.translator import translator, TranslationOptions

from apps.draftlaw.models import DraftLaw, DraftLawDiscussion, DraftLawChild


class DraftLawTranslationOptions(TranslationOptions):
    fields = ('title', 'initiator', 'author', 'status', 'summary', 'full_text',)


class DraftLawDiscussionTranslationOptions(TranslationOptions):
    fields = ('place',)


class DraftLawChildTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(DraftLaw, DraftLawTranslationOptions)
translator.register(DraftLawDiscussion, DraftLawDiscussionTranslationOptions)
translator.register(DraftLawChild, DraftLawChildTranslationOptions)
