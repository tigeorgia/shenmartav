# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from django.contrib import admin
from django.db import models

from imagekit.admin import AdminThumbnail

from apps.podcasting.forms import AdminShowForm, AdminEpisodeForm
from apps.podcasting.models import Show, Episode, Enclosure
from apps.podcasting.utils.twitter import can_tweet

from modeltranslation.admin import TranslationAdmin
from tinymce.widgets import TinyMCE


class ShowAdmin(TranslationAdmin):
    form = AdminShowForm

    list_display = ("title", "slug", "show_site", "published_flag", "admin_thumbnail")
    list_filter = ("title", "published", "site")
    admin_thumbnail = AdminThumbnail(image_field="admin_thumb_sm")

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
    }

    if can_tweet():
        fields.append("tweet_text")

    def published_flag(self, obj):
        return bool(obj.published)
    published_flag.short_description = _("Published")
    published_flag.boolean = True

    def show_site(self, obj):
        return obj.site.name
    show_site.short_description = "Site"


class EpisodeAdmin(TranslationAdmin):
    form = AdminEpisodeForm

    list_display = ("title", "show", "slug", "episode_site", "published_flag", "admin_thumbnail")
    list_filter = ("show", "published")
    admin_thumbnail = AdminThumbnail(image_field="admin_thumb_sm")

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
    }

    if can_tweet():
        readonly_fields = ("tweet_text",)

    def published_flag(self, obj):
        return bool(obj.published)
    published_flag.short_description = _("Published")
    published_flag.boolean = True

    def episode_site(self, obj):
        return obj.show.site.name
    episode_site.short_description = "Site"

    def save_form(self, request, form, change):
        # this is done for explicitness that we want form.save to commit
        # form.save doesn't take a commit kwarg for this reason
        return form.save()


class EnclosureAdmin(admin.ModelAdmin):
    list_display = ("episode", "mime", "url")
    list_filter = ("episode",)


admin.site.register(Show, ShowAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Enclosure, EnclosureAdmin)
