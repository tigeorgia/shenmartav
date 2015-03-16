# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SMSRegister.email'
        db.add_column('smsregister_smsregister', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SMSRegister.email'
        db.delete_column('smsregister_smsregister', 'email')


    models = {
        'smsregister.smsregister': {
            'Meta': {'ordering': "('-name',)", 'object_name': 'SMSRegister'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'groups': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'phone_number': ('django.db.models.fields.TextField', [], {}),
            'selected_language': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['smsregister']