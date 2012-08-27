# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'DeclarationGift.giver_rel'
        db.alter_column('incomedeclaration_declarationgift', 'giver_rel', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationGift.name'
        db.alter_column('incomedeclaration_declarationgift', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationGift.desc_value'
        db.alter_column('incomedeclaration_declarationgift', 'desc_value', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationGift.desc_value_en'
        db.alter_column('incomedeclaration_declarationgift', 'desc_value_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationGift.desc_value_ka'
        db.alter_column('incomedeclaration_declarationgift', 'desc_value_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationGift.name_en'
        db.alter_column('incomedeclaration_declarationgift', 'name_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationGift.name_ka'
        db.alter_column('incomedeclaration_declarationgift', 'name_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationGift.giver_rel_ka'
        db.alter_column('incomedeclaration_declarationgift', 'giver_rel_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationGift.giver_rel_en'
        db.alter_column('incomedeclaration_declarationgift', 'giver_rel_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationEntrepreneurial.particn_type'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'particn_type', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationEntrepreneurial.particn_date_en'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'particn_date_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationEntrepreneurial.name'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationEntrepreneurial.corp_name_addr_ka'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'corp_name_addr_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationEntrepreneurial.register_agency'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'register_agency', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationEntrepreneurial.corp_name_addr'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'corp_name_addr', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationEntrepreneurial.corp_name_addr_en'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'corp_name_addr_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationEntrepreneurial.register_agency_ka'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'register_agency_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationEntrepreneurial.register_agency_en'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'register_agency_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationEntrepreneurial.particn_type_en'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'particn_type_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationEntrepreneurial.particn_type_ka'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'particn_type_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationEntrepreneurial.particn_date_ka'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'particn_date_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationEntrepreneurial.particn_date'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'particn_date', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationEntrepreneurial.income_rec_ka'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'income_rec_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationEntrepreneurial.name_en'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'name_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationEntrepreneurial.name_ka'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'name_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationEntrepreneurial.income_rec'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'income_rec', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationEntrepreneurial.income_rec_en'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'income_rec_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationFamily.pob_ka'
        db.alter_column('incomedeclaration_declarationfamily', 'pob_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationFamily.pob_en'
        db.alter_column('incomedeclaration_declarationfamily', 'pob_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationFamily.surname'
        db.alter_column('incomedeclaration_declarationfamily', 'surname', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationFamily.name'
        db.alter_column('incomedeclaration_declarationfamily', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationFamily.dob'
        db.alter_column('incomedeclaration_declarationfamily', 'dob', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationFamily.relation_en'
        db.alter_column('incomedeclaration_declarationfamily', 'relation_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationFamily.surname_ka'
        db.alter_column('incomedeclaration_declarationfamily', 'surname_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationFamily.surname_en'
        db.alter_column('incomedeclaration_declarationfamily', 'surname_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationFamily.relation_ka'
        db.alter_column('incomedeclaration_declarationfamily', 'relation_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationFamily.dob_en'
        db.alter_column('incomedeclaration_declarationfamily', 'dob_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationFamily.dob_ka'
        db.alter_column('incomedeclaration_declarationfamily', 'dob_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationFamily.name_en'
        db.alter_column('incomedeclaration_declarationfamily', 'name_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationFamily.name_ka'
        db.alter_column('incomedeclaration_declarationfamily', 'name_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationFamily.pob'
        db.alter_column('incomedeclaration_declarationfamily', 'pob', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationFamily.relation'
        db.alter_column('incomedeclaration_declarationfamily', 'relation', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationProperty.co_owners_ka'
        db.alter_column('incomedeclaration_declarationproperty', 'co_owners_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationProperty.name_shares_ka'
        db.alter_column('incomedeclaration_declarationproperty', 'name_shares_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationProperty.description'
        db.alter_column('incomedeclaration_declarationproperty', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationProperty.co_owners_en'
        db.alter_column('incomedeclaration_declarationproperty', 'co_owners_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationProperty.name_shares_en'
        db.alter_column('incomedeclaration_declarationproperty', 'name_shares_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationProperty.name_shares'
        db.alter_column('incomedeclaration_declarationproperty', 'name_shares', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationProperty.description_en'
        db.alter_column('incomedeclaration_declarationproperty', 'description_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationProperty.prop_type_ka'
        db.alter_column('incomedeclaration_declarationproperty', 'prop_type_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationProperty.co_owners'
        db.alter_column('incomedeclaration_declarationproperty', 'co_owners', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationProperty.description_ka'
        db.alter_column('incomedeclaration_declarationproperty', 'description_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationProperty.prop_type'
        db.alter_column('incomedeclaration_declarationproperty', 'prop_type', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationProperty.prop_type_en'
        db.alter_column('incomedeclaration_declarationproperty', 'prop_type_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationBiography.work_contact_en'
        db.alter_column('incomedeclaration_declarationbiography', 'work_contact_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationBiography.place_dob'
        db.alter_column('incomedeclaration_declarationbiography', 'place_dob', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationBiography.position_en'
        db.alter_column('incomedeclaration_declarationbiography', 'position_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationBiography.position_ka'
        db.alter_column('incomedeclaration_declarationbiography', 'position_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationBiography.work_contact'
        db.alter_column('incomedeclaration_declarationbiography', 'work_contact', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationBiography.position'
        db.alter_column('incomedeclaration_declarationbiography', 'position', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationBiography.place_dob_ka'
        db.alter_column('incomedeclaration_declarationbiography', 'place_dob_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationBiography.place_dob_en'
        db.alter_column('incomedeclaration_declarationbiography', 'place_dob_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationBiography.work_contact_ka'
        db.alter_column('incomedeclaration_declarationbiography', 'work_contact_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationContract.desc_value_en'
        db.alter_column('incomedeclaration_declarationcontract', 'desc_value_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationContract.desc_value'
        db.alter_column('incomedeclaration_declarationcontract', 'desc_value', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationContract.name'
        db.alter_column('incomedeclaration_declarationcontract', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationContract.desc_value_ka'
        db.alter_column('incomedeclaration_declarationcontract', 'desc_value_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationContract.financial_result'
        db.alter_column('incomedeclaration_declarationcontract', 'financial_result', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationContract.date_period_agency_ka'
        db.alter_column('incomedeclaration_declarationcontract', 'date_period_agency_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationContract.financial_result_ka'
        db.alter_column('incomedeclaration_declarationcontract', 'financial_result_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationContract.financial_result_en'
        db.alter_column('incomedeclaration_declarationcontract', 'financial_result_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationContract.date_period_agency'
        db.alter_column('incomedeclaration_declarationcontract', 'date_period_agency', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationContract.name_en'
        db.alter_column('incomedeclaration_declarationcontract', 'name_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationContract.name_ka'
        db.alter_column('incomedeclaration_declarationcontract', 'name_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationContract.date_period_agency_en'
        db.alter_column('incomedeclaration_declarationcontract', 'date_period_agency_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationRealEstate.co_owners_ka'
        db.alter_column('incomedeclaration_declarationrealestate', 'co_owners_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationRealEstate.name_shares_ka'
        db.alter_column('incomedeclaration_declarationrealestate', 'name_shares_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationRealEstate.co_owners_en'
        db.alter_column('incomedeclaration_declarationrealestate', 'co_owners_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationRealEstate.name_shares_en'
        db.alter_column('incomedeclaration_declarationrealestate', 'name_shares_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationRealEstate.loc_area'
        db.alter_column('incomedeclaration_declarationrealestate', 'loc_area', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationRealEstate.name_shares'
        db.alter_column('incomedeclaration_declarationrealestate', 'name_shares', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationRealEstate.loc_area_en'
        db.alter_column('incomedeclaration_declarationrealestate', 'loc_area_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationRealEstate.prop_type_ka'
        db.alter_column('incomedeclaration_declarationrealestate', 'prop_type_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationRealEstate.co_owners'
        db.alter_column('incomedeclaration_declarationrealestate', 'co_owners', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationRealEstate.prop_type'
        db.alter_column('incomedeclaration_declarationrealestate', 'prop_type', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationRealEstate.prop_type_en'
        db.alter_column('incomedeclaration_declarationrealestate', 'prop_type_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationRealEstate.loc_area_ka'
        db.alter_column('incomedeclaration_declarationrealestate', 'loc_area_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationCash.amt_currency'
        db.alter_column('incomedeclaration_declarationcash', 'amt_currency', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationCash.amt_currency_ka'
        db.alter_column('incomedeclaration_declarationcash', 'amt_currency_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationCash.name'
        db.alter_column('incomedeclaration_declarationcash', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationCash.name_en'
        db.alter_column('incomedeclaration_declarationcash', 'name_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationCash.name_ka'
        db.alter_column('incomedeclaration_declarationcash', 'name_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationCash.amt_currency_en'
        db.alter_column('incomedeclaration_declarationcash', 'amt_currency_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationWage.name'
        db.alter_column('incomedeclaration_declarationwage', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationWage.desc_job'
        db.alter_column('incomedeclaration_declarationwage', 'desc_job', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationWage.desc_job_en'
        db.alter_column('incomedeclaration_declarationwage', 'desc_job_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationWage.desc_job_ka'
        db.alter_column('incomedeclaration_declarationwage', 'desc_job_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationWage.desc_workplace_ka'
        db.alter_column('incomedeclaration_declarationwage', 'desc_workplace_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationWage.desc_workplace'
        db.alter_column('incomedeclaration_declarationwage', 'desc_workplace', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationWage.income_rec_en'
        db.alter_column('incomedeclaration_declarationwage', 'income_rec_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationWage.income_rec_ka'
        db.alter_column('incomedeclaration_declarationwage', 'income_rec_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationWage.name_en'
        db.alter_column('incomedeclaration_declarationwage', 'name_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationWage.name_ka'
        db.alter_column('incomedeclaration_declarationwage', 'name_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationWage.income_rec'
        db.alter_column('incomedeclaration_declarationwage', 'income_rec', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationWage.desc_workplace_en'
        db.alter_column('incomedeclaration_declarationwage', 'desc_workplace_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationOtherInclExpense.amount_en'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'amount_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationOtherInclExpense.recip_issuer'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'recip_issuer', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationOtherInclExpense.type_en'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'type_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationOtherInclExpense.type_ka'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'type_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationOtherInclExpense.amount_ka'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'amount_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationOtherInclExpense.amount'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'amount', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationOtherInclExpense.recip_issuer_en'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'recip_issuer_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationOtherInclExpense.recip_issuer_ka'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'recip_issuer_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationOtherInclExpense.type'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'type', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationSecurity.name_ka'
        db.alter_column('incomedeclaration_declarationsecurity', 'name_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationSecurity.name'
        db.alter_column('incomedeclaration_declarationsecurity', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationSecurity.issuer'
        db.alter_column('incomedeclaration_declarationsecurity', 'issuer', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationSecurity.type_en'
        db.alter_column('incomedeclaration_declarationsecurity', 'type_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationSecurity.price'
        db.alter_column('incomedeclaration_declarationsecurity', 'price', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationSecurity.issuer_en'
        db.alter_column('incomedeclaration_declarationsecurity', 'issuer_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationSecurity.issuer_ka'
        db.alter_column('incomedeclaration_declarationsecurity', 'issuer_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationSecurity.type_ka'
        db.alter_column('incomedeclaration_declarationsecurity', 'type_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationSecurity.name_en'
        db.alter_column('incomedeclaration_declarationsecurity', 'name_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationSecurity.quantity'
        db.alter_column('incomedeclaration_declarationsecurity', 'quantity', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationSecurity.type'
        db.alter_column('incomedeclaration_declarationsecurity', 'type', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationSecurity.price_ka'
        db.alter_column('incomedeclaration_declarationsecurity', 'price_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationSecurity.price_en'
        db.alter_column('incomedeclaration_declarationsecurity', 'price_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationDeposit.name_ka'
        db.alter_column('incomedeclaration_declarationdeposit', 'name_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationDeposit.name'
        db.alter_column('incomedeclaration_declarationdeposit', 'name', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationDeposit.balance_en'
        db.alter_column('incomedeclaration_declarationdeposit', 'balance_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationDeposit.type_en'
        db.alter_column('incomedeclaration_declarationdeposit', 'type_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationDeposit.bank_en'
        db.alter_column('incomedeclaration_declarationdeposit', 'bank_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationDeposit.type_ka'
        db.alter_column('incomedeclaration_declarationdeposit', 'type_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationDeposit.bank_ka'
        db.alter_column('incomedeclaration_declarationdeposit', 'bank_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationDeposit.balance_ka'
        db.alter_column('incomedeclaration_declarationdeposit', 'balance_ka', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationDeposit.name_en'
        db.alter_column('incomedeclaration_declarationdeposit', 'name_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'DeclarationDeposit.balance'
        db.alter_column('incomedeclaration_declarationdeposit', 'balance', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationDeposit.type'
        db.alter_column('incomedeclaration_declarationdeposit', 'type', self.gf('django.db.models.fields.TextField')())

        # Changing field 'DeclarationDeposit.bank'
        db.alter_column('incomedeclaration_declarationdeposit', 'bank', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'DeclarationGift.giver_rel'
        db.alter_column('incomedeclaration_declarationgift', 'giver_rel', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'DeclarationGift.name'
        db.alter_column('incomedeclaration_declarationgift', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationGift.desc_value'
        db.alter_column('incomedeclaration_declarationgift', 'desc_value', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationGift.desc_value_en'
        db.alter_column('incomedeclaration_declarationgift', 'desc_value_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationGift.desc_value_ka'
        db.alter_column('incomedeclaration_declarationgift', 'desc_value_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationGift.name_en'
        db.alter_column('incomedeclaration_declarationgift', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationGift.name_ka'
        db.alter_column('incomedeclaration_declarationgift', 'name_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationGift.giver_rel_ka'
        db.alter_column('incomedeclaration_declarationgift', 'giver_rel_ka', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationGift.giver_rel_en'
        db.alter_column('incomedeclaration_declarationgift', 'giver_rel_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationEntrepreneurial.particn_type'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'particn_type', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'DeclarationEntrepreneurial.particn_date_en'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'particn_date_en', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

        # Changing field 'DeclarationEntrepreneurial.name'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationEntrepreneurial.corp_name_addr_ka'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'corp_name_addr_ka', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

        # Changing field 'DeclarationEntrepreneurial.register_agency'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'register_agency', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'DeclarationEntrepreneurial.corp_name_addr'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'corp_name_addr', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'DeclarationEntrepreneurial.corp_name_addr_en'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'corp_name_addr_en', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

        # Changing field 'DeclarationEntrepreneurial.register_agency_ka'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'register_agency_ka', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

        # Changing field 'DeclarationEntrepreneurial.register_agency_en'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'register_agency_en', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

        # Changing field 'DeclarationEntrepreneurial.particn_type_en'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'particn_type_en', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

        # Changing field 'DeclarationEntrepreneurial.particn_type_ka'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'particn_type_ka', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

        # Changing field 'DeclarationEntrepreneurial.particn_date_ka'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'particn_date_ka', self.gf('django.db.models.fields.CharField')(max_length=512, null=True))

        # Changing field 'DeclarationEntrepreneurial.particn_date'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'particn_date', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'DeclarationEntrepreneurial.income_rec_ka'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'income_rec_ka', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationEntrepreneurial.name_en'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationEntrepreneurial.name_ka'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'name_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationEntrepreneurial.income_rec'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'income_rec', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'DeclarationEntrepreneurial.income_rec_en'
        db.alter_column('incomedeclaration_declarationentrepreneurial', 'income_rec_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationFamily.pob_ka'
        db.alter_column('incomedeclaration_declarationfamily', 'pob_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationFamily.pob_en'
        db.alter_column('incomedeclaration_declarationfamily', 'pob_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationFamily.surname'
        db.alter_column('incomedeclaration_declarationfamily', 'surname', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationFamily.name'
        db.alter_column('incomedeclaration_declarationfamily', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationFamily.dob'
        db.alter_column('incomedeclaration_declarationfamily', 'dob', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationFamily.relation_en'
        db.alter_column('incomedeclaration_declarationfamily', 'relation_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationFamily.surname_ka'
        db.alter_column('incomedeclaration_declarationfamily', 'surname_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationFamily.surname_en'
        db.alter_column('incomedeclaration_declarationfamily', 'surname_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationFamily.relation_ka'
        db.alter_column('incomedeclaration_declarationfamily', 'relation_ka', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationFamily.dob_en'
        db.alter_column('incomedeclaration_declarationfamily', 'dob_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationFamily.dob_ka'
        db.alter_column('incomedeclaration_declarationfamily', 'dob_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationFamily.name_en'
        db.alter_column('incomedeclaration_declarationfamily', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationFamily.name_ka'
        db.alter_column('incomedeclaration_declarationfamily', 'name_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationFamily.pob'
        db.alter_column('incomedeclaration_declarationfamily', 'pob', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationFamily.relation'
        db.alter_column('incomedeclaration_declarationfamily', 'relation', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'DeclarationProperty.co_owners_ka'
        db.alter_column('incomedeclaration_declarationproperty', 'co_owners_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationProperty.name_shares_ka'
        db.alter_column('incomedeclaration_declarationproperty', 'name_shares_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationProperty.description'
        db.alter_column('incomedeclaration_declarationproperty', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationProperty.co_owners_en'
        db.alter_column('incomedeclaration_declarationproperty', 'co_owners_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationProperty.name_shares_en'
        db.alter_column('incomedeclaration_declarationproperty', 'name_shares_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationProperty.name_shares'
        db.alter_column('incomedeclaration_declarationproperty', 'name_shares', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationProperty.description_en'
        db.alter_column('incomedeclaration_declarationproperty', 'description_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationProperty.prop_type_ka'
        db.alter_column('incomedeclaration_declarationproperty', 'prop_type_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationProperty.co_owners'
        db.alter_column('incomedeclaration_declarationproperty', 'co_owners', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationProperty.description_ka'
        db.alter_column('incomedeclaration_declarationproperty', 'description_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationProperty.prop_type'
        db.alter_column('incomedeclaration_declarationproperty', 'prop_type', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationProperty.prop_type_en'
        db.alter_column('incomedeclaration_declarationproperty', 'prop_type_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationBiography.work_contact_en'
        db.alter_column('incomedeclaration_declarationbiography', 'work_contact_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationBiography.place_dob'
        db.alter_column('incomedeclaration_declarationbiography', 'place_dob', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationBiography.position_en'
        db.alter_column('incomedeclaration_declarationbiography', 'position_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationBiography.position_ka'
        db.alter_column('incomedeclaration_declarationbiography', 'position_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationBiography.work_contact'
        db.alter_column('incomedeclaration_declarationbiography', 'work_contact', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationBiography.position'
        db.alter_column('incomedeclaration_declarationbiography', 'position', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationBiography.place_dob_ka'
        db.alter_column('incomedeclaration_declarationbiography', 'place_dob_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationBiography.place_dob_en'
        db.alter_column('incomedeclaration_declarationbiography', 'place_dob_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationBiography.work_contact_ka'
        db.alter_column('incomedeclaration_declarationbiography', 'work_contact_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationContract.desc_value_en'
        db.alter_column('incomedeclaration_declarationcontract', 'desc_value_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationContract.desc_value'
        db.alter_column('incomedeclaration_declarationcontract', 'desc_value', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationContract.name'
        db.alter_column('incomedeclaration_declarationcontract', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationContract.desc_value_ka'
        db.alter_column('incomedeclaration_declarationcontract', 'desc_value_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationContract.financial_result'
        db.alter_column('incomedeclaration_declarationcontract', 'financial_result', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationContract.date_period_agency_ka'
        db.alter_column('incomedeclaration_declarationcontract', 'date_period_agency_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationContract.financial_result_ka'
        db.alter_column('incomedeclaration_declarationcontract', 'financial_result_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationContract.financial_result_en'
        db.alter_column('incomedeclaration_declarationcontract', 'financial_result_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationContract.date_period_agency'
        db.alter_column('incomedeclaration_declarationcontract', 'date_period_agency', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationContract.name_en'
        db.alter_column('incomedeclaration_declarationcontract', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationContract.name_ka'
        db.alter_column('incomedeclaration_declarationcontract', 'name_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationContract.date_period_agency_en'
        db.alter_column('incomedeclaration_declarationcontract', 'date_period_agency_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationRealEstate.co_owners_ka'
        db.alter_column('incomedeclaration_declarationrealestate', 'co_owners_ka', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

        # Changing field 'DeclarationRealEstate.name_shares_ka'
        db.alter_column('incomedeclaration_declarationrealestate', 'name_shares_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationRealEstate.co_owners_en'
        db.alter_column('incomedeclaration_declarationrealestate', 'co_owners_en', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

        # Changing field 'DeclarationRealEstate.name_shares_en'
        db.alter_column('incomedeclaration_declarationrealestate', 'name_shares_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationRealEstate.loc_area'
        db.alter_column('incomedeclaration_declarationrealestate', 'loc_area', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationRealEstate.name_shares'
        db.alter_column('incomedeclaration_declarationrealestate', 'name_shares', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationRealEstate.loc_area_en'
        db.alter_column('incomedeclaration_declarationrealestate', 'loc_area_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationRealEstate.prop_type_ka'
        db.alter_column('incomedeclaration_declarationrealestate', 'prop_type_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationRealEstate.co_owners'
        db.alter_column('incomedeclaration_declarationrealestate', 'co_owners', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'DeclarationRealEstate.prop_type'
        db.alter_column('incomedeclaration_declarationrealestate', 'prop_type', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationRealEstate.prop_type_en'
        db.alter_column('incomedeclaration_declarationrealestate', 'prop_type_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationRealEstate.loc_area_ka'
        db.alter_column('incomedeclaration_declarationrealestate', 'loc_area_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationCash.amt_currency'
        db.alter_column('incomedeclaration_declarationcash', 'amt_currency', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'DeclarationCash.amt_currency_ka'
        db.alter_column('incomedeclaration_declarationcash', 'amt_currency_ka', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationCash.name'
        db.alter_column('incomedeclaration_declarationcash', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationCash.name_en'
        db.alter_column('incomedeclaration_declarationcash', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationCash.name_ka'
        db.alter_column('incomedeclaration_declarationcash', 'name_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationCash.amt_currency_en'
        db.alter_column('incomedeclaration_declarationcash', 'amt_currency_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationWage.name'
        db.alter_column('incomedeclaration_declarationwage', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationWage.desc_job'
        db.alter_column('incomedeclaration_declarationwage', 'desc_job', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationWage.desc_job_en'
        db.alter_column('incomedeclaration_declarationwage', 'desc_job_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationWage.desc_job_ka'
        db.alter_column('incomedeclaration_declarationwage', 'desc_job_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationWage.desc_workplace_ka'
        db.alter_column('incomedeclaration_declarationwage', 'desc_workplace_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationWage.desc_workplace'
        db.alter_column('incomedeclaration_declarationwage', 'desc_workplace', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationWage.income_rec_en'
        db.alter_column('incomedeclaration_declarationwage', 'income_rec_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationWage.income_rec_ka'
        db.alter_column('incomedeclaration_declarationwage', 'income_rec_ka', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationWage.name_en'
        db.alter_column('incomedeclaration_declarationwage', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationWage.name_ka'
        db.alter_column('incomedeclaration_declarationwage', 'name_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationWage.income_rec'
        db.alter_column('incomedeclaration_declarationwage', 'income_rec', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'DeclarationWage.desc_workplace_en'
        db.alter_column('incomedeclaration_declarationwage', 'desc_workplace_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationOtherInclExpense.amount_en'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'amount_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationOtherInclExpense.recip_issuer'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'recip_issuer', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationOtherInclExpense.type_en'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'type_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationOtherInclExpense.type_ka'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'type_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationOtherInclExpense.amount_ka'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'amount_ka', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationOtherInclExpense.amount'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'amount', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'DeclarationOtherInclExpense.recip_issuer_en'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'recip_issuer_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationOtherInclExpense.recip_issuer_ka'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'recip_issuer_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationOtherInclExpense.type'
        db.alter_column('incomedeclaration_declarationotherinclexpense', 'type', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationSecurity.name_ka'
        db.alter_column('incomedeclaration_declarationsecurity', 'name_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationSecurity.name'
        db.alter_column('incomedeclaration_declarationsecurity', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationSecurity.issuer'
        db.alter_column('incomedeclaration_declarationsecurity', 'issuer', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'DeclarationSecurity.type_en'
        db.alter_column('incomedeclaration_declarationsecurity', 'type_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationSecurity.price'
        db.alter_column('incomedeclaration_declarationsecurity', 'price', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'DeclarationSecurity.issuer_en'
        db.alter_column('incomedeclaration_declarationsecurity', 'issuer_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationSecurity.issuer_ka'
        db.alter_column('incomedeclaration_declarationsecurity', 'issuer_ka', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationSecurity.type_ka'
        db.alter_column('incomedeclaration_declarationsecurity', 'type_ka', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationSecurity.name_en'
        db.alter_column('incomedeclaration_declarationsecurity', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'DeclarationSecurity.quantity'
        db.alter_column('incomedeclaration_declarationsecurity', 'quantity', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'DeclarationSecurity.type'
        db.alter_column('incomedeclaration_declarationsecurity', 'type', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'DeclarationSecurity.price_ka'
        db.alter_column('incomedeclaration_declarationsecurity', 'price_ka', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationSecurity.price_en'
        db.alter_column('incomedeclaration_declarationsecurity', 'price_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationDeposit.name_ka'
        db.alter_column('incomedeclaration_declarationdeposit', 'name_ka', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

        # Changing field 'DeclarationDeposit.name'
        db.alter_column('incomedeclaration_declarationdeposit', 'name', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'DeclarationDeposit.balance_en'
        db.alter_column('incomedeclaration_declarationdeposit', 'balance_en', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationDeposit.type_en'
        db.alter_column('incomedeclaration_declarationdeposit', 'type_en', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

        # Changing field 'DeclarationDeposit.bank_en'
        db.alter_column('incomedeclaration_declarationdeposit', 'bank_en', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

        # Changing field 'DeclarationDeposit.type_ka'
        db.alter_column('incomedeclaration_declarationdeposit', 'type_ka', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

        # Changing field 'DeclarationDeposit.bank_ka'
        db.alter_column('incomedeclaration_declarationdeposit', 'bank_ka', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

        # Changing field 'DeclarationDeposit.balance_ka'
        db.alter_column('incomedeclaration_declarationdeposit', 'balance_ka', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'DeclarationDeposit.name_en'
        db.alter_column('incomedeclaration_declarationdeposit', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

        # Changing field 'DeclarationDeposit.balance'
        db.alter_column('incomedeclaration_declarationdeposit', 'balance', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'DeclarationDeposit.type'
        db.alter_column('incomedeclaration_declarationdeposit', 'type', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'DeclarationDeposit.bank'
        db.alter_column('incomedeclaration_declarationdeposit', 'bank', self.gf('django.db.models.fields.CharField')(max_length=1024))

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
            'place_dob': ('django.db.models.fields.TextField', [], {}),
            'place_dob_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'place_dob_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.TextField', [], {}),
            'position_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'position_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'work_contact': ('django.db.models.fields.TextField', [], {}),
            'work_contact_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'work_contact_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationcash': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationCash'},
            'amt_currency': ('django.db.models.fields.TextField', [], {}),
            'amt_currency_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'amt_currency_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cash'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationcontract': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationContract'},
            'date_period_agency': ('django.db.models.fields.TextField', [], {}),
            'date_period_agency_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_period_agency_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contracts'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'desc_value': ('django.db.models.fields.TextField', [], {}),
            'desc_value_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_value_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financial_result': ('django.db.models.fields.TextField', [], {}),
            'financial_result_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financial_result_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationdeposit': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationDeposit'},
            'balance': ('django.db.models.fields.TextField', [], {}),
            'balance_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'balance_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bank': ('django.db.models.fields.TextField', [], {}),
            'bank_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bank_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deposits'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.TextField', [], {}),
            'type_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationentrepreneurial': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationEntrepreneurial'},
            'corp_name_addr': ('django.db.models.fields.TextField', [], {}),
            'corp_name_addr_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'corp_name_addr_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entrepreneurials'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income_rec': ('django.db.models.fields.TextField', [], {}),
            'income_rec_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'income_rec_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'particn_date': ('django.db.models.fields.TextField', [], {}),
            'particn_date_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'particn_date_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'particn_type': ('django.db.models.fields.TextField', [], {}),
            'particn_type_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'particn_type_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_agency': ('django.db.models.fields.TextField', [], {}),
            'register_agency_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_agency_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationfamily': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationFamily'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'family'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'dob': ('django.db.models.fields.TextField', [], {}),
            'dob_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dob_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob': ('django.db.models.fields.TextField', [], {}),
            'pob_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'relation': ('django.db.models.fields.TextField', [], {}),
            'relation_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'relation_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.TextField', [], {}),
            'surname_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'surname_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationgift': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationGift'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gifts'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'desc_value': ('django.db.models.fields.TextField', [], {}),
            'desc_value_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_value_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'giver_rel': ('django.db.models.fields.TextField', [], {}),
            'giver_rel_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'giver_rel_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationotherinclexpense': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationOtherInclExpense'},
            'amount': ('django.db.models.fields.TextField', [], {}),
            'amount_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'amount_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'otherinclexpenses'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recip_issuer': ('django.db.models.fields.TextField', [], {}),
            'recip_issuer_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'recip_issuer_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.TextField', [], {}),
            'type_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationproperty': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationProperty'},
            'co_owners': ('django.db.models.fields.TextField', [], {}),
            'co_owners_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'co_owners_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'properties'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_shares': ('django.db.models.fields.TextField', [], {}),
            'name_shares_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_shares_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prop_type': ('django.db.models.fields.TextField', [], {}),
            'prop_type_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prop_type_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationrealestate': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationRealEstate'},
            'co_owners': ('django.db.models.fields.TextField', [], {}),
            'co_owners_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'co_owners_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'realestates'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loc_area': ('django.db.models.fields.TextField', [], {}),
            'loc_area_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'loc_area_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_shares': ('django.db.models.fields.TextField', [], {}),
            'name_shares_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_shares_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prop_type': ('django.db.models.fields.TextField', [], {}),
            'prop_type_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prop_type_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationsecurity': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationSecurity'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'securities'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.TextField', [], {}),
            'issuer_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'issuer_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.TextField', [], {}),
            'price_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'price_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.TextField', [], {}),
            'type_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationwage': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationWage'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wages'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'desc_job': ('django.db.models.fields.TextField', [], {}),
            'desc_job_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_job_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_workplace': ('django.db.models.fields.TextField', [], {}),
            'desc_workplace_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_workplace_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income_rec': ('django.db.models.fields.TextField', [], {}),
            'income_rec_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'income_rec_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.incomedeclaration': {
            'Meta': {'ordering': "('decl_id',)", 'object_name': 'IncomeDeclaration'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'decl_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'incomedeclaration'", 'null': 'True', 'to': "orm['representative.Representative']"}),
            'scrape_date': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        'incomedeclaration.incomedeclarationpluginconf': {
            'Meta': {'object_name': 'IncomeDeclarationPluginConf', 'db_table': "'cmsplugin_incomedeclarationpluginconf'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Income Declarations'", 'max_length': '32'})
        },
        'popit.organisation': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Organisation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ended': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '300'}),
            'started': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'summary_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'summary_ka': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'popit.person': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Person'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'date_of_death': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'description_ka': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'representative.party': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Party', '_ormbases': ['popit.Organisation']},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'organisation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['popit.Organisation']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'representative.representative': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Representative', '_ormbases': ['popit.Person']},
            'answered': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'attendance_record': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'committee': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'committee_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'committee_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_majoritarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other_income': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'representatives'", 'null': 'True', 'to': "orm['representative.Party']"}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['popit.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pob': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'representatives'", 'null': 'True', 'to': "orm['representative.Unit']"}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'representative.unit': {
            'Meta': {'object_name': 'Unit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parties': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'unit'", 'symmetrical': 'False', 'to': "orm['representative.Party']"}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['incomedeclaration']