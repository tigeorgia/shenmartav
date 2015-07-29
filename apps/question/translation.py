from modeltranslation.translator import translator, TranslationOptions
from apps.question.models import Question


class QuestionTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'question', 'answer',)


translator.register(Question, QuestionTranslationOptions)
