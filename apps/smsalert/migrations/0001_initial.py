# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SMSAlert'
        db.create_table('smsalert_smsalert', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_ka', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_sent', self.gf('django.db.models.fields.DateField')()),
            ('date_created', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
        ))
        db.send_create_signal('smsalert', ['SMSAlert'])

        # Adding M2M table for field draftlaws on 'SMSAlert'
        db.create_table('smsalert_smsalert_draftlaws', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('smsalert', models.ForeignKey(orm['smsalert.smsalert'], null=False)),
            ('draftlaw', models.ForeignKey(orm['draftlaw.draftlaw'], null=False))
        ))
        db.create_unique('smsalert_smsalert_draftlaws', ['smsalert_id', 'draftlaw_id'])


    def backwards(self, orm):
        # Deleting model 'SMSAlert'
        db.delete_table('smsalert_smsalert')

        # Removing M2M table for field draftlaws on 'SMSAlert'
        db.delete_table('smsalert_smsalert_draftlaws')


    models = {
        'draftlaw.draftlaw': {
            'Meta': {'ordering': "('-bill_number',)", 'object_name': 'DraftLaw'},
            'author': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'author_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'author_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bill_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bureau_date': ('django.db.models.fields.DateField', [], {}),
            'enable_annotations': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'enacted_text_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'full_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'full_text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'full_text_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'full_text_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiator': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'initiator_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initiator_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'law_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'moderate_annotations': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'related_1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'related_2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'related_3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'related_4': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'related_5': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'shortstatus': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'summary_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'summary_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'title_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'voting_record': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'voting_on'", 'null': 'True', 'to': "orm['votingrecord.VotingRecord']"})
        },
        'smsalert.smsalert': {
            'Meta': {'object_name': 'SMSAlert'},
            'date_created': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'date_sent': ('django.db.models.fields.DateField', [], {}),
            'draftlaws': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sms_alerts'", 'symmetrical': 'False', 'to': "orm['draftlaw.DraftLaw']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
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

    complete_apps = ['smsalert']