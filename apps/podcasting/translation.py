from modeltranslation.translator import translator, TranslationOptions
from apps.podcasting.models import Episode, Show


class ShowTranslationOptions(TranslationOptions):
    fields = ('organization', 'author_text', 'title', 'subtitle', 'description',
              'keywords',)


class EpisodeTranslationOptions(TranslationOptions):
    fields = ('author_text', 'title', 'subtitle', 'description',)


translator.register(Show, ShowTranslationOptions)
translator.register(Episode, EpisodeTranslationOptions)
