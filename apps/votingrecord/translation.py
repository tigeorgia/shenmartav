from modeltranslation.translator import translator, TranslationOptions

from apps.votingrecord.models import VotingRecord


class VotingRecordTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(VotingRecord, VotingRecordTranslationOptions)
