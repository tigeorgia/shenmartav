# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DraftLawChild.title_en'
        db.add_column('draftlaw_draftlawchild', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLawChild.title_ka'
        db.add_column('draftlaw_draftlawchild', 'title_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLaw.title_en'
        db.add_column('draftlaw_draftlaw', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLaw.title_ka'
        db.add_column('draftlaw_draftlaw', 'title_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLaw.initiator_en'
        db.add_column('draftlaw_draftlaw', 'initiator_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLaw.initiator_ka'
        db.add_column('draftlaw_draftlaw', 'initiator_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLaw.author_en'
        db.add_column('draftlaw_draftlaw', 'author_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLaw.author_ka'
        db.add_column('draftlaw_draftlaw', 'author_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLaw.status_en'
        db.add_column('draftlaw_draftlaw', 'status_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLaw.status_ka'
        db.add_column('draftlaw_draftlaw', 'status_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLaw.summary_en'
        db.add_column('draftlaw_draftlaw', 'summary_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLaw.summary_ka'
        db.add_column('draftlaw_draftlaw', 'summary_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLaw.full_text_en'
        db.add_column('draftlaw_draftlaw', 'full_text_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLaw.full_text_ka'
        db.add_column('draftlaw_draftlaw', 'full_text_ka',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLawDiscussion.place_en'
        db.add_column('draftlaw_draftlawdiscussion', 'place_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DraftLawDiscussion.place_ka'
        db.add_column('draftlaw_draftlawdiscussion', 'place_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DraftLawChild.title_en'
        db.delete_column('draftlaw_draftlawchild', 'title_en')

        # Deleting field 'DraftLawChild.title_ka'
        db.delete_column('draftlaw_draftlawchild', 'title_ka')

        # Deleting field 'DraftLaw.title_en'
        db.delete_column('draftlaw_draftlaw', 'title_en')

        # Deleting field 'DraftLaw.title_ka'
        db.delete_column('draftlaw_draftlaw', 'title_ka')

        # Deleting field 'DraftLaw.initiator_en'
        db.delete_column('draftlaw_draftlaw', 'initiator_en')

        # Deleting field 'DraftLaw.initiator_ka'
        db.delete_column('draftlaw_draftlaw', 'initiator_ka')

        # Deleting field 'DraftLaw.author_en'
        db.delete_column('draftlaw_draftlaw', 'author_en')

        # Deleting field 'DraftLaw.author_ka'
        db.delete_column('draftlaw_draftlaw', 'author_ka')

        # Deleting field 'DraftLaw.status_en'
        db.delete_column('draftlaw_draftlaw', 'status_en')

        # Deleting field 'DraftLaw.status_ka'
        db.delete_column('draftlaw_draftlaw', 'status_ka')

        # Deleting field 'DraftLaw.summary_en'
        db.delete_column('draftlaw_draftlaw', 'summary_en')

        # Deleting field 'DraftLaw.summary_ka'
        db.delete_column('draftlaw_draftlaw', 'summary_ka')

        # Deleting field 'DraftLaw.full_text_en'
        db.delete_column('draftlaw_draftlaw', 'full_text_en')

        # Deleting field 'DraftLaw.full_text_ka'
        db.delete_column('draftlaw_draftlaw', 'full_text_ka')

        # Deleting field 'DraftLawDiscussion.place_en'
        db.delete_column('draftlaw_draftlawdiscussion', 'place_en')

        # Deleting field 'DraftLawDiscussion.place_ka'
        db.delete_column('draftlaw_draftlawdiscussion', 'place_ka')


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
        }
    }

    complete_apps = ['draftlaw']