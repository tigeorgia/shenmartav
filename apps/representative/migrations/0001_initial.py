# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Representative'
        db.create_table('representative_representative', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['popit.Person'], unique=True, primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('party', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(default='n', max_length=1)),
            ('committee', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('faction', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_majoritarian', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('electoral_district', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('elected', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pob', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('family_status', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('education', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('contact_address_phone', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('attendance_record', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('salary', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
            ('expenses', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('property_assets', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('answered', self.gf('django.db.models.fields.FloatField')(default=0, null=True)),
        ))
        db.send_create_signal('representative', ['Representative'])

        # Adding model 'AdditionalInformation'
        db.create_table('representative_additionalinformation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('representative', self.gf('django.db.models.fields.related.ForeignKey')(related_name='additional_information', null=True, to=orm['representative.Representative'])),
            ('value', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('representative', ['AdditionalInformation'])

        # Adding model 'RandomRepresentative'
        db.create_table('representative_randomrepresentative', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_set', self.gf('django.db.models.fields.DateTimeField')()),
            ('representative', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['representative.Representative'], null=True)),
        ))
        db.send_create_signal('representative', ['RandomRepresentative'])

        # Adding model 'RepresentativePluginConf'
        db.create_table('cmsplugin_representativepluginconf', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Representative', max_length=32)),
        ))
        db.send_create_signal('representative', ['RepresentativePluginConf'])


    def backwards(self, orm):
        
        # Deleting model 'Representative'
        db.delete_table('representative_representative')

        # Deleting model 'AdditionalInformation'
        db.delete_table('representative_additionalinformation')

        # Deleting model 'RandomRepresentative'
        db.delete_table('representative_randomrepresentative')

        # Deleting model 'RepresentativePluginConf'
        db.delete_table('cmsplugin_representativepluginconf')


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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'representative.additionalinformation': {
            'Meta': {'object_name': 'AdditionalInformation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'additional_information'", 'null': 'True', 'to': "orm['representative.Representative']"}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True'})
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
            'contact_address_phone': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'is_majoritarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'party': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['popit.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pob': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
