from modeltranslation.translator import translator, TranslationOptions

from apps.basic.blog.models import Category, Post, BlogRoll


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'tease',)


class BlogRollTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Category, CategoryTranslationOptions)
translator.register(Post, PostTranslationOptions)
translator.register(BlogRoll, BlogRollTranslationOptions)
