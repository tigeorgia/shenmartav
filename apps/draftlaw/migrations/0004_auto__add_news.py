# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table('draftlaw_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 6, 18, 0, 0))),
            ('body', self.gf('django.db.models.fields.TextField')(default='')),
            ('body_en', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('body_ka', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
        ))
        db.send_create_signal('draftlaw', ['News'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table('draftlaw_news')


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
        'draftlaw.draftlaw': {
            'Meta': {'ordering': "('-bill_number',)", 'object_name': 'DraftLaw'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'author_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'author_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bill_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bureau_date': ('django.db.models.fields.DateField', [], {}),
            'enable_annotations': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'enacted_text_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'full_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'full_text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'full_text_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'full_text_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiator': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'initiator_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initiator_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'law_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'moderate_annotations': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'related_1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'related_2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'related_3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'related_4': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'related_5': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'shortstatus': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'sms_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sms_ka': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'summary_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'summary_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'voting_record': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'voting_on'", 'null': 'True', 'to': "orm['votingrecord.VotingRecord']"})
        },
        'draftlaw.draftlawchild': {
            'Meta': {'object_name': 'DraftLawChild'},
            'bill_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'enacted_text_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'law_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'to': "orm['draftlaw.DraftLaw']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'voting_record': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'voting_on_child'", 'null': 'True', 'to': "orm['votingrecord.VotingRecord']"})
        },
        'draftlaw.draftlawdiscussion': {
            'Meta': {'object_name': 'DraftLawDiscussion'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'draftlaw': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'discussions'", 'to': "orm['draftlaw.DraftLaw']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'place_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'place_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stage': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'draftlaw.draftlawpluginconf': {
            'Meta': {'object_name': 'DraftLawPluginConf', 'db_table': "'cmsplugin_draftlawpluginconf'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Draft Laws'", 'max_length': '32'})
        },
        'draftlaw.news': {
            'Meta': {'object_name': 'News'},
            'body': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'body_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'body_ka': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 6, 18, 0, 0)'})
        },
        'votingrecord.votingrecord': {
            'Meta': {'ordering': "['-date', '-number']", 'object_name': 'VotingRecord'},
            'amended_by': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'amending'", 'null': 'True', 'to': "orm['votingrecord.VotingRecord']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kan_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'scrape_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['draftlaw']