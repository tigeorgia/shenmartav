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
        
        # Adding model 'IncomeDeclaration'
        db.create_table('incomedeclaration_incomedeclaration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('decl_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('scrape_date', self.gf('django.db.models.fields.DateField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('representative', self.gf('django.db.models.fields.related.ForeignKey')(related_name='incomedeclaration', null=True, to=orm['representative.Representative'])),
        ))
        db.send_create_signal('incomedeclaration', ['IncomeDeclaration'])

        # Adding model 'DeclarationBiography'
        db.create_table('incomedeclaration_declarationbiography', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declaration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='biographies', to=orm['incomedeclaration.IncomeDeclaration'])),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('work_contact', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('place_dob', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('incomedeclaration', ['DeclarationBiography'])

        # Adding model 'DeclarationCash'
        db.create_table('incomedeclaration_declarationcash', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declaration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cash', to=orm['incomedeclaration.IncomeDeclaration'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('amt_currency', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('incomedeclaration', ['DeclarationCash'])

        # Adding model 'DeclarationContract'
        db.create_table('incomedeclaration_declarationcontract', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declaration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contracts', to=orm['incomedeclaration.IncomeDeclaration'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('desc_value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_period_agency', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('financial_result', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('incomedeclaration', ['DeclarationContract'])

        # Adding model 'DeclarationDeposit'
        db.create_table('incomedeclaration_declarationdeposit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declaration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='deposits', to=orm['incomedeclaration.IncomeDeclaration'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('bank', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('balance', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('incomedeclaration', ['DeclarationDeposit'])

        # Adding model 'DeclarationEntrepreneurial'
        db.create_table('incomedeclaration_declarationentrepreneurial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declaration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entrepreneurials', to=orm['incomedeclaration.IncomeDeclaration'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('corp_name_addr', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('particn_type', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('register_agency', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('particn_date', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('income_rec', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('incomedeclaration', ['DeclarationEntrepreneurial'])

        # Adding model 'DeclarationFamily'
        db.create_table('incomedeclaration_declarationfamily', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declaration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='family', to=orm['incomedeclaration.IncomeDeclaration'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pob', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dob', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('relation', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('incomedeclaration', ['DeclarationFamily'])

        # Adding model 'DeclarationGift'
        db.create_table('incomedeclaration_declarationgift', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declaration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gifts', to=orm['incomedeclaration.IncomeDeclaration'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('desc_value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('giver_rel', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('incomedeclaration', ['DeclarationGift'])

        # Adding model 'DeclarationOtherInclExpense'
        db.create_table('incomedeclaration_declarationotherinclexpense', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declaration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='otherinclexpenses', to=orm['incomedeclaration.IncomeDeclaration'])),
            ('recip_issuer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('incomedeclaration', ['DeclarationOtherInclExpense'])

        # Adding model 'DeclarationProperty'
        db.create_table('incomedeclaration_declarationproperty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declaration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='properties', to=orm['incomedeclaration.IncomeDeclaration'])),
            ('name_shares', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('prop_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('co_owners', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('incomedeclaration', ['DeclarationProperty'])

        # Adding model 'DeclarationRealEstate'
        db.create_table('incomedeclaration_declarationrealestate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declaration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='realestates', to=orm['incomedeclaration.IncomeDeclaration'])),
            ('name_shares', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('prop_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('loc_area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('co_owners', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('incomedeclaration', ['DeclarationRealEstate'])

        # Adding model 'DeclarationSecurity'
        db.create_table('incomedeclaration_declarationsecurity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declaration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='securities', to=orm['incomedeclaration.IncomeDeclaration'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('issuer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('incomedeclaration', ['DeclarationSecurity'])

        # Adding model 'DeclarationWage'
        db.create_table('incomedeclaration_declarationwage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('declaration', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wages', to=orm['incomedeclaration.IncomeDeclaration'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('desc_workplace', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('desc_job', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('income_rec', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('incomedeclaration', ['DeclarationWage'])

        # Adding model 'IncomeDeclarationPluginConf'
        db.create_table('cmsplugin_incomedeclarationpluginconf', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=u'Income Declarations', max_length=32)),
        ))
        db.send_create_signal('incomedeclaration', ['IncomeDeclarationPluginConf'])


    def backwards(self, orm):
        
        # Deleting model 'IncomeDeclaration'
        db.delete_table('incomedeclaration_incomedeclaration')

        # Deleting model 'DeclarationBiography'
        db.delete_table('incomedeclaration_declarationbiography')

        # Deleting model 'DeclarationCash'
        db.delete_table('incomedeclaration_declarationcash')

        # Deleting model 'DeclarationContract'
        db.delete_table('incomedeclaration_declarationcontract')

        # Deleting model 'DeclarationDeposit'
        db.delete_table('incomedeclaration_declarationdeposit')

        # Deleting model 'DeclarationEntrepreneurial'
        db.delete_table('incomedeclaration_declarationentrepreneurial')

        # Deleting model 'DeclarationFamily'
        db.delete_table('incomedeclaration_declarationfamily')

        # Deleting model 'DeclarationGift'
        db.delete_table('incomedeclaration_declarationgift')

        # Deleting model 'DeclarationOtherInclExpense'
        db.delete_table('incomedeclaration_declarationotherinclexpense')

        # Deleting model 'DeclarationProperty'
        db.delete_table('incomedeclaration_declarationproperty')

        # Deleting model 'DeclarationRealEstate'
        db.delete_table('incomedeclaration_declarationrealestate')

        # Deleting model 'DeclarationSecurity'
        db.delete_table('incomedeclaration_declarationsecurity')

        # Deleting model 'DeclarationWage'
        db.delete_table('incomedeclaration_declarationwage')

        # Deleting model 'IncomeDeclarationPluginConf'
        db.delete_table('cmsplugin_incomedeclarationpluginconf')


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
        'incomedeclaration.declarationbiography': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationBiography'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'biographies'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place_dob': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'work_contact': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'incomedeclaration.declarationcash': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationCash'},
            'amt_currency': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cash'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'incomedeclaration.declarationcontract': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationContract'},
            'date_period_agency': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contracts'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'desc_value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'financial_result': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'incomedeclaration.declarationdeposit': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationDeposit'},
            'balance': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'bank': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deposits'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'incomedeclaration.declarationentrepreneurial': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationEntrepreneurial'},
            'corp_name_addr': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entrepreneurials'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income_rec': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'particn_date': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'particn_type': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'register_agency': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'incomedeclaration.declarationfamily': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationFamily'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'family'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'dob': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pob': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'relation': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'incomedeclaration.declarationgift': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationGift'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gifts'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'desc_value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'giver_rel': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'incomedeclaration.declarationotherinclexpense': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationOtherInclExpense'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'otherinclexpenses'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recip_issuer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'incomedeclaration.declarationproperty': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationProperty'},
            'co_owners': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'properties'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_shares': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prop_type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'incomedeclaration.declarationrealestate': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationRealEstate'},
            'co_owners': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'realestates'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loc_area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_shares': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prop_type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'incomedeclaration.declarationsecurity': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationSecurity'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'securities'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'incomedeclaration.declarationwage': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationWage'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wages'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'desc_job': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'desc_workplace': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income_rec': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'incomedeclaration.incomedeclaration': {
            'Meta': {'ordering': "('decl_id',)", 'object_name': 'IncomeDeclaration'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'decl_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'incomedeclaration'", 'null': 'True', 'to': "orm['representative.Representative']"}),
            'scrape_date': ('django.db.models.fields.DateField', [], {})
        },
        'incomedeclaration.incomedeclarationpluginconf': {
            'Meta': {'object_name': 'IncomeDeclarationPluginConf', 'db_table': "'cmsplugin_incomedeclarationpluginconf'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Income Declarations'", 'max_length': '32'})
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
        }
    }

    complete_apps = ['incomedeclaration']
