# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'VotingRecord.kan_id_chars'
        db.alter_column('votingrecord_votingrecord', 'kan_id_chars', self.gf('django.db.models.fields.CharField')(default='', max_length=512))

        # Changing field 'VotingRecord.name'
        db.alter_column('votingrecord_votingrecord', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=512))

        # Changing field 'VotingRecord.number'
        db.alter_column('votingrecord_votingrecord', 'number', self.gf('django.db.models.fields.CharField')(default='', max_length=32))

        # Changing field 'VotingRecord.url'
        db.alter_column('votingrecord_votingrecord', 'url', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'VotingRecordResult.css'
        db.alter_column('votingrecord_votingrecordresult', 'css', self.gf('django.db.models.fields.CharField')(default='', max_length=32))

        # Changing field 'VotingRecordAmendment.number'
        db.alter_column('votingrecord_votingrecordamendment', 'number', self.gf('django.db.models.fields.CharField')(default='', max_length=32))

    def backwards(self, orm):

        # Changing field 'VotingRecord.kan_id_chars'
        db.alter_column('votingrecord_votingrecord', 'kan_id_chars', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

        # Changing field 'VotingRecord.name'
        db.alter_column('votingrecord_votingrecord', 'name', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

        # Changing field 'VotingRecord.number'
        db.alter_column('votingrecord_votingrecord', 'number', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'VotingRecord.url'
        db.alter_column('votingrecord_votingrecord', 'url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'VotingRecordResult.css'
        db.alter_column('votingrecord_votingrecordresult', 'css', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'VotingRecordAmendment.number'
        db.alter_column('votingrecord_votingrecordamendment', 'number', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

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
        'popit.organisation': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Organisation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ended': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '300'}),
            'started': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'summary_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'summary_ka': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'popit.person': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Person'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'date_of_death': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'description_ka': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'representative.cabinet': {
            'Meta': {'ordering': "['position']", 'object_name': 'Cabinet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'representative.faction': {
            'Meta': {'object_name': 'Faction'},
            'cabinet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'faction'", 'null': 'True', 'to': "orm['representative.Cabinet']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'representative.party': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Party', '_ormbases': ['popit.Organisation']},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'organisation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['popit.Organisation']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'representative.representative': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Representative', '_ormbases': ['popit.Person']},
            'answered': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'committee': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'committee_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'committee_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_address_phone_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'education_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elected_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'electoral_district_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'entrepreneurial_salary': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'expenses': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expenses_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'representatives'", 'null': 'True', 'to': "orm['representative.Faction']"}),
            'family_status': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'is_majoritarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'main_salary': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'other_income': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'representatives'", 'null': 'True', 'to': "orm['representative.Party']"}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['popit.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pob': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pob_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'property_assets_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'submission_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'terms': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'representatives'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['representative.Term']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'representatives'", 'null': 'True', 'to': "orm['representative.Unit']"})
        },
        'representative.term': {
            'Meta': {'object_name': 'Term'},
            'end': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {})
        },
        'representative.unit': {
            'Meta': {'object_name': 'Unit'},
            'active_term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'unit_active'", 'null': 'True', 'to': "orm['representative.Term']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inactive_terms': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'unit_inactive'", 'blank': 'True', 'to': "orm['representative.Term']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parties': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'unit'", 'symmetrical': 'False', 'to': "orm['representative.Party']"}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'votingrecord.votingrecord': {
            'Meta': {'ordering': "['-date', '-number']", 'object_name': 'VotingRecord'},
            'amended_by': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'amending'", 'null': 'True', 'to': "orm['votingrecord.VotingRecord']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kan_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'kan_id_chars': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'scrape_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'votingrecord.votingrecordamendment': {
            'Meta': {'object_name': 'VotingRecordAmendment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'amendments'", 'to': "orm['votingrecord.VotingRecord']"})
        },
        'votingrecord.votingrecordpluginconf': {
            'Meta': {'object_name': 'VotingRecordPluginConf', 'db_table': "'cmsplugin_votingrecordpluginconf'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Voting Records'", 'max_length': '32'})
        },
        'votingrecord.votingrecordresult': {
            'Meta': {'ordering': "['-vote']", 'object_name': 'VotingRecordResult'},
            'css': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'results'", 'to': "orm['votingrecord.VotingRecord']"}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votingresults'", 'null': 'True', 'to': "orm['representative.Representative']"}),
            'session': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'totalsession': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'vote': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'vote_en': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'vote_ka': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['votingrecord']