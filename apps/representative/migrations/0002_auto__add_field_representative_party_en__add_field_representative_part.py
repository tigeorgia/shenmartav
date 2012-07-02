# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Representative.party_en'
        db.add_column('representative_representative', 'party_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.party_ka'
        db.add_column('representative_representative', 'party_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.committee_en'
        db.add_column('representative_representative', 'committee_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.committee_ka'
        db.add_column('representative_representative', 'committee_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.faction_en'
        db.add_column('representative_representative', 'faction_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.faction_ka'
        db.add_column('representative_representative', 'faction_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.electoral_district_en'
        db.add_column('representative_representative', 'electoral_district_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.electoral_district_ka'
        db.add_column('representative_representative', 'electoral_district_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.elected_en'
        db.add_column('representative_representative', 'elected_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.elected_ka'
        db.add_column('representative_representative', 'elected_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.pob_en'
        db.add_column('representative_representative', 'pob_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.pob_ka'
        db.add_column('representative_representative', 'pob_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.family_status_en'
        db.add_column('representative_representative', 'family_status_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.family_status_ka'
        db.add_column('representative_representative', 'family_status_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.education_en'
        db.add_column('representative_representative', 'education_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.education_ka'
        db.add_column('representative_representative', 'education_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.contact_address_phone_en'
        db.add_column('representative_representative', 'contact_address_phone_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.contact_address_phone_ka'
        db.add_column('representative_representative', 'contact_address_phone_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.expenses_en'
        db.add_column('representative_representative', 'expenses_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.expenses_ka'
        db.add_column('representative_representative', 'expenses_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.property_assets_en'
        db.add_column('representative_representative', 'property_assets_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Representative.property_assets_ka'
        db.add_column('representative_representative', 'property_assets_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'AdditionalInformation.value_en'
        db.add_column('representative_additionalinformation', 'value_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'AdditionalInformation.value_ka'
        db.add_column('representative_additionalinformation', 'value_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Representative.party_en'
        db.delete_column('representative_representative', 'party_en')

        # Deleting field 'Representative.party_ka'
        db.delete_column('representative_representative', 'party_ka')

        # Deleting field 'Representative.committee_en'
        db.delete_column('representative_representative', 'committee_en')

        # Deleting field 'Representative.committee_ka'
        db.delete_column('representative_representative', 'committee_ka')

        # Deleting field 'Representative.faction_en'
        db.delete_column('representative_representative', 'faction_en')

        # Deleting field 'Representative.faction_ka'
        db.delete_column('representative_representative', 'faction_ka')

        # Deleting field 'Representative.electoral_district_en'
        db.delete_column('representative_representative', 'electoral_district_en')

        # Deleting field 'Representative.electoral_district_ka'
        db.delete_column('representative_representative', 'electoral_district_ka')

        # Deleting field 'Representative.elected_en'
        db.delete_column('representative_representative', 'elected_en')

        # Deleting field 'Representative.elected_ka'
        db.delete_column('representative_representative', 'elected_ka')

        # Deleting field 'Representative.pob_en'
        db.delete_column('representative_representative', 'pob_en')

        # Deleting field 'Representative.pob_ka'
        db.delete_column('representative_representative', 'pob_ka')

        # Deleting field 'Representative.family_status_en'
        db.delete_column('representative_representative', 'family_status_en')

        # Deleting field 'Representative.family_status_ka'
        db.delete_column('representative_representative', 'family_status_ka')

        # Deleting field 'Representative.education_en'
        db.delete_column('representative_representative', 'education_en')

        # Deleting field 'Representative.education_ka'
        db.delete_column('representative_representative', 'education_ka')

        # Deleting field 'Representative.contact_address_phone_en'
        db.delete_column('representative_representative', 'contact_address_phone_en')

        # Deleting field 'Representative.contact_address_phone_ka'
        db.delete_column('representative_representative', 'contact_address_phone_ka')

        # Deleting field 'Representative.expenses_en'
        db.delete_column('representative_representative', 'expenses_en')

        # Deleting field 'Representative.expenses_ka'
        db.delete_column('representative_representative', 'expenses_ka')

        # Deleting field 'Representative.property_assets_en'
        db.delete_column('representative_representative', 'property_assets_en')

        # Deleting field 'Representative.property_assets_ka'
        db.delete_column('representative_representative', 'property_assets_ka')

        # Deleting field 'AdditionalInformation.value_en'
        db.delete_column('representative_additionalinformation', 'value_en')

        # Deleting field 'AdditionalInformation.value_ka'
        db.delete_column('representative_additionalinformation', 'value_ka')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'popit.person': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Person'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'date_of_death': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'description': ('markitup.fields.MarkupField', [], {'default': "''", 'no_rendered_field': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'representative.additionalinformation': {
            'Meta': {'object_name': 'AdditionalInformation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'additional_information'", 'null': 'True', 'to': "orm['representative.Representative']"}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'value_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'value_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'representative.randomrepresentative': {
            'Meta': {'object_name': 'RandomRepresentative'},
            'date_set': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['representative.Representative']", 'null': 'True'})
        },
        'representative.representative': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Representative', '_ormbases': ['popit.Person']},
            'answered': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'attendance_record': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'committee': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'committee_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'committee_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'is_majoritarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'party': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'party_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'party_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['popit.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pob': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'default': "'n'", 'max_length': '1'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'representative.representativepluginconf': {
            'Meta': {'object_name': 'RepresentativePluginConf', 'db_table': "'cmsplugin_representativepluginconf'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Representative'", 'max_length': '32'})
        }
    }

    complete_apps = ['representative']