from django.contrib import admin
#from sorl.thumbnail.admin import AdminImageMixin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from popit import models

def create_admin_link_for(obj, link_text):
    return u'<a href="%s">%s</a>' % ( obj.get_admin_url(), link_text )

class PositionInlineAdmin(TranslationTabularInline):
    model      = models.Position
    extra      = 3    # do not set to zero as the autocomplete does not work in inlines
    can_delete = True
    fields     = [ 'person', 'organisation', 'type', 'title_en', 'title_ka', 'place_en', 'place_ka', 'start_date', 'end_date' ]

# People

class PersonNameInlineAdmin(TranslationTabularInline):
    model = models.PersonName
class PersonCodeInlineAdmin(admin.TabularInline):
    model = models.PersonCode
class PersonDataInlineAdmin(admin.TabularInline):
    fields = [ 'key', 'value' ]
    model = models.PersonData

class PersonDataKeyAdmin(admin.ModelAdmin):
    pass

#class PersonAdmin(AdminImageMixin, admin.ModelAdmin):
#class PersonAdmin (admin.ModelAdmin):
class PersonAdmin (TranslationAdmin):
    inlines       = [ PersonNameInlineAdmin, PersonCodeInlineAdmin, PersonDataInlineAdmin, PositionInlineAdmin ]
    list_display  = [ 'slug', 'name', 'date_of_birth' ]
    search_fields = [ 'names__name' ]
    exclude = ('description',)

#admin.site.register( models.Person, PersonAdmin )
#admin.site.register( models.PersonDataKey, PersonDataKeyAdmin )

# Orgs

class OrgNameInlineAdmin(TranslationTabularInline):
    model = models.OrganisationName
class OrgCodeInlineAdmin(admin.TabularInline):
    model = models.OrganisationCode
class OrgDataInlineAdmin(admin.TabularInline):
    fields = [ 'key', 'value' ]
    model = models.OrganisationData

class OrgDataKeyAdmin(admin.ModelAdmin):
    pass

class OrganisationAdmin(TranslationAdmin):
    inlines       = [ OrgNameInlineAdmin, OrgCodeInlineAdmin, OrgDataInlineAdmin, PositionInlineAdmin ]
    list_display  = [ 'slug', 'name' ]
    search_fields = [ 'names__name' ]

#admin.site.register( models.Organisation, OrganisationAdmin )
#admin.site.register( models.OrganisationDataKey, OrgDataKeyAdmin )

# Positions

class PositionCategoryAdmin(admin.ModelAdmin):
    pass
class PositionDataKeyAdmin(admin.ModelAdmin):
    pass
class PositionDataInlineAdmin(admin.TabularInline):
    fields = [ 'key', 'value' ]
    model = models.PositionData

class PositionTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = [ 'name' ]

class PositionAdmin(TranslationAdmin):
    list_display  = [ 'id', 'Person', 'Organisation', 'Type', 'title', 'place', 'start_date', 'end_date' ]
    search_fields = [ 'person__name', 'organisation__name', 'type__name' ]
    list_filter   = [ 'type__name' ]
    readonly_fields = ['sorting_start_date','sorting_end_date']
    inlines       = [ PositionDataInlineAdmin ]

    def Person(self, obj):
        return create_admin_link_for( obj.person, obj.person.name )
    Person.allow_tags = True

    def Organisation(self, obj):
        if not obj.organisation and obj.type and obj.type.organisation:
            return '[' + create_admin_link_for(obj.type.organisation, obj.type.organisation.name) + ']'
        return create_admin_link_for(obj.organisation, obj.organisation.name)
    Organisation.allow_tags = True

    def Type(self, obj):
        return create_admin_link_for(obj.type, obj.type.name)
    Type.allow_tags = True

#admin.site.register( models.Position, PositionAdmin )
#admin.site.register( models.PositionType, PositionTypeAdmin )
#admin.site.register( models.PositionDataKey, PositionDataKeyAdmin )
#admin.site.register( models.PositionCategory, PositionCategoryAdmin )

#admin.site.register( models.CodeType )
