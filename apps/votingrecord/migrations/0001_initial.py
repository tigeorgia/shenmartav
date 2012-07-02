# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    depends_on = (
        ("representative", "0001_initial"),
    )


    def forwards(self, orm):
        
        # Adding model 'VotingRecord'
        db.create_table('votingrecord_votingrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kan_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('scrape_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512, null=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
        ))
        db.send_create_signal('votingrecord', ['VotingRecord'])

        # Adding M2M table for field amended_by on 'VotingRecord'
        db.create_table('votingrecord_votingrecord_amended_by', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_votingrecord', models.ForeignKey(orm['votingrecord.votingrecord'], null=False)),
            ('to_votingrecord', models.ForeignKey(orm['votingrecord.votingrecord'], null=False))
        ))
        db.create_unique('votingrecord_votingrecord_amended_by', ['from_votingrecord_id', 'to_votingrecord_id'])

        # Adding model 'VotingRecordResult'
        db.create_table('votingrecord_votingrecordresult', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(related_name='results', to=orm['votingrecord.VotingRecord'])),
            ('vote', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('representative', self.gf('django.db.models.fields.related.ForeignKey')(related_name='votingresults', null=True, to=orm['representative.Representative'])),
            ('css', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
        ))
        db.send_create_signal('votingrecord', ['VotingRecordResult'])

        # Adding model 'VotingRecordAmendment'
        db.create_table('votingrecord_votingrecordamendment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(related_name='amendments', to=orm['votingrecord.VotingRecord'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
        ))
        db.send_create_signal('votingrecord', ['VotingRecordAmendment'])

        # Adding model 'VotingRecordPluginConf'
        db.create_table('cmsplugin_votingrecordpluginconf', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Voting Records', max_length=32)),
        ))
        db.send_create_signal('votingrecord', ['VotingRecordPluginConf'])


    def backwards(self, orm):
        
        # Deleting model 'VotingRecord'
        db.delete_table('votingrecord_votingrecord')

        # Removing M2M table for field amended_by on 'VotingRecord'
        db.delete_table('votingrecord_votingrecord_amended_by')

        # Deleting model 'VotingRecordResult'
        db.delete_table('votingrecord_votingrecordresult')

        # Deleting model 'VotingRecordAmendment'
        db.delete_table('votingrecord_votingrecordamendment')

        # Deleting model 'VotingRecordPluginConf'
        db.delete_table('cmsplugin_votingrecordpluginconf')


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
        'votingrecord.votingrecord': {
            'Meta': {'ordering': "['-date', '-number']", 'object_name': 'VotingRecord'},
            'amended_by': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'amending'", 'null': 'True', 'to': "orm['votingrecord.VotingRecord']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kan_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'scrape_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'votingrecord.votingrecordamendment': {
            'Meta': {'object_name': 'VotingRecordAmendment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'amendments'", 'to': "orm['votingrecord.VotingRecord']"})
        },
        'votingrecord.votingrecordpluginconf': {
            'Meta': {'object_name': 'VotingRecordPluginConf', 'db_table': "'cmsplugin_votingrecordpluginconf'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Voting Records'", 'max_length': '32'})
        },
        'votingrecord.votingrecordresult': {
            'Meta': {'ordering': "['-vote']", 'object_name': 'VotingRecordResult'},
            'css': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'results'", 'to': "orm['votingrecord.VotingRecord']"}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votingresults'", 'null': 'True', 'to': "orm['representative.Representative']"}),
            'vote': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['votingrecord']
