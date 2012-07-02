# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    depends_on = (
        ("representative", "0001_initial"),
        ("votingrecord", "0001_initial"),
    )


    def forwards(self, orm):
        
        # Adding model 'DraftLaw'
        db.create_table('draftlaw_draftlaw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bureau_date', self.gf('django.db.models.fields.DateField')()),
            ('bill_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('initiator', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('shortstatus', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sms_ka', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sms_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('full_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('full_text_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('enacted_text_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('law_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('voting_record', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='voting_on', null=True, to=orm['votingrecord.VotingRecord'])),
            ('related_1', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('related_2', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('related_3', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('related_4', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('related_5', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('enable_annotations', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('moderate_annotations', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
        ))
        db.send_create_signal('draftlaw', ['DraftLaw'])

        # Adding model 'DraftLawDiscussion'
        db.create_table('draftlaw_draftlawdiscussion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('draftlaw', self.gf('django.db.models.fields.related.ForeignKey')(related_name='discussions', to=orm['draftlaw.DraftLaw'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('stage', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('draftlaw', ['DraftLawDiscussion'])

        # Adding model 'DraftLawChild'
        db.create_table('draftlaw_draftlawchild', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', to=orm['draftlaw.DraftLaw'])),
            ('bill_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('enacted_text_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('law_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('voting_record', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='voting_on_child', null=True, to=orm['votingrecord.VotingRecord'])),
        ))
        db.send_create_signal('draftlaw', ['DraftLawChild'])

        # Adding model 'DraftLawPluginConf'
        db.create_table('cmsplugin_draftlawpluginconf', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Draft Laws', max_length=32)),
        ))
        db.send_create_signal('draftlaw', ['DraftLawPluginConf'])


    def backwards(self, orm):
        
        # Deleting model 'DraftLaw'
        db.delete_table('draftlaw_draftlaw')

        # Deleting model 'DraftLawDiscussion'
        db.delete_table('draftlaw_draftlawdiscussion')

        # Deleting model 'DraftLawChild'
        db.delete_table('draftlaw_draftlawchild')

        # Deleting model 'DraftLawPluginConf'
        db.delete_table('cmsplugin_draftlawpluginconf')


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
            'bill_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'bureau_date': ('django.db.models.fields.DateField', [], {}),
            'enable_annotations': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'enacted_text_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'full_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'full_text_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initiator': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'voting_record': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'voting_on_child'", 'null': 'True', 'to': "orm['votingrecord.VotingRecord']"})
        },
        'draftlaw.draftlawdiscussion': {
            'Meta': {'object_name': 'DraftLawDiscussion'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'draftlaw': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'discussions'", 'to': "orm['draftlaw.DraftLaw']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
