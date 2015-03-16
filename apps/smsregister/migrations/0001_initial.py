# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SMSRegister'
        db.create_table('smsregister_smsregister', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('selected_language', self.gf('django.db.models.fields.TextField')()),
            ('date_created', self.gf('django.db.models.fields.TextField')()),
            ('groups', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('smsregister', ['SMSRegister'])


    def backwards(self, orm):
        # Deleting model 'SMSRegister'
        db.delete_table('smsregister_smsregister')


    models = {
        'smsregister.smsregister': {
            'Meta': {'ordering': "('-name',)", 'object_name': 'SMSRegister'},
            'date_created': ('django.db.models.fields.TextField', [], {}),
            'groups': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'selected_language': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['smsregister']