# -*- coding: utf-8 -*-

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.db import models

from basic.blog.models import *
from tinymce.widgets import TinyMCE


class CategoryAdmin (TranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category, CategoryAdmin)

class PostAdmin (TranslationAdmin):
    list_display  = ('title', 'publish', 'status')
    list_filter   = ('publish', 'categories', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
    }

    def add_view(self, request, form_url="", extra_context=None):
        # request.GET is immutable
        data = request.GET.copy()
        data['allow_comments'] = False
        data['author'] = 2 # user shenmartav
        request.GET = data
        return super(PostAdmin, self).add_view(request, form_url="", extra_context=extra_context)
admin.site.register(Post, PostAdmin)


class BlogRollAdmin (TranslationAdmin):
    list_display = ('name', 'url', 'sort_order',)
    list_editable = ('sort_order',)
admin.site.register(BlogRoll)
