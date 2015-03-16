# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SMSRegister.date_created'
        db.delete_column('smsregister_smsregister', 'date_created')

        # Adding field 'SMSRegister.phone_number'
        db.add_column('smsregister_smsregister', 'phone_number',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'SMSRegister.date_created'
        db.add_column('smsregister_smsregister', 'date_created',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'SMSRegister.phone_number'
        db.delete_column('smsregister_smsregister', 'phone_number')


    models = {
        'smsregister.smsregister': {
            'Meta': {'ordering': "('-name',)", 'object_name': 'SMSRegister'},
            'groups': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'phone_number': ('django.db.models.fields.TextField', [], {}),
            'selected_language': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['smsregister']