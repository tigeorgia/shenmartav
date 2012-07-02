# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DeclarationGift.name_en'
        db.add_column('incomedeclaration_declarationgift', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationGift.name_ka'
        db.add_column('incomedeclaration_declarationgift', 'name_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationGift.desc_value_en'
        db.add_column('incomedeclaration_declarationgift', 'desc_value_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationGift.desc_value_ka'
        db.add_column('incomedeclaration_declarationgift', 'desc_value_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationGift.giver_rel_en'
        db.add_column('incomedeclaration_declarationgift', 'giver_rel_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationGift.giver_rel_ka'
        db.add_column('incomedeclaration_declarationgift', 'giver_rel_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationEntrepreneurial.name_en'
        db.add_column('incomedeclaration_declarationentrepreneurial', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationEntrepreneurial.name_ka'
        db.add_column('incomedeclaration_declarationentrepreneurial', 'name_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationEntrepreneurial.corp_name_addr_en'
        db.add_column('incomedeclaration_declarationentrepreneurial', 'corp_name_addr_en',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationEntrepreneurial.corp_name_addr_ka'
        db.add_column('incomedeclaration_declarationentrepreneurial', 'corp_name_addr_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationEntrepreneurial.particn_type_en'
        db.add_column('incomedeclaration_declarationentrepreneurial', 'particn_type_en',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationEntrepreneurial.particn_type_ka'
        db.add_column('incomedeclaration_declarationentrepreneurial', 'particn_type_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationEntrepreneurial.register_agency_en'
        db.add_column('incomedeclaration_declarationentrepreneurial', 'register_agency_en',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationEntrepreneurial.register_agency_ka'
        db.add_column('incomedeclaration_declarationentrepreneurial', 'register_agency_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationEntrepreneurial.particn_date_en'
        db.add_column('incomedeclaration_declarationentrepreneurial', 'particn_date_en',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationEntrepreneurial.particn_date_ka'
        db.add_column('incomedeclaration_declarationentrepreneurial', 'particn_date_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationEntrepreneurial.income_rec_en'
        db.add_column('incomedeclaration_declarationentrepreneurial', 'income_rec_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationEntrepreneurial.income_rec_ka'
        db.add_column('incomedeclaration_declarationentrepreneurial', 'income_rec_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationFamily.name_en'
        db.add_column('incomedeclaration_declarationfamily', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationFamily.name_ka'
        db.add_column('incomedeclaration_declarationfamily', 'name_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationFamily.surname_en'
        db.add_column('incomedeclaration_declarationfamily', 'surname_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationFamily.surname_ka'
        db.add_column('incomedeclaration_declarationfamily', 'surname_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationFamily.pob_en'
        db.add_column('incomedeclaration_declarationfamily', 'pob_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationFamily.pob_ka'
        db.add_column('incomedeclaration_declarationfamily', 'pob_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationFamily.dob_en'
        db.add_column('incomedeclaration_declarationfamily', 'dob_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationFamily.dob_ka'
        db.add_column('incomedeclaration_declarationfamily', 'dob_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationFamily.relation_en'
        db.add_column('incomedeclaration_declarationfamily', 'relation_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationFamily.relation_ka'
        db.add_column('incomedeclaration_declarationfamily', 'relation_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationProperty.name_shares_en'
        db.add_column('incomedeclaration_declarationproperty', 'name_shares_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationProperty.name_shares_ka'
        db.add_column('incomedeclaration_declarationproperty', 'name_shares_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationProperty.prop_type_en'
        db.add_column('incomedeclaration_declarationproperty', 'prop_type_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationProperty.prop_type_ka'
        db.add_column('incomedeclaration_declarationproperty', 'prop_type_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationProperty.description_en'
        db.add_column('incomedeclaration_declarationproperty', 'description_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationProperty.description_ka'
        db.add_column('incomedeclaration_declarationproperty', 'description_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationProperty.co_owners_en'
        db.add_column('incomedeclaration_declarationproperty', 'co_owners_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationProperty.co_owners_ka'
        db.add_column('incomedeclaration_declarationproperty', 'co_owners_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationBiography.position_en'
        db.add_column('incomedeclaration_declarationbiography', 'position_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationBiography.position_ka'
        db.add_column('incomedeclaration_declarationbiography', 'position_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationBiography.work_contact_en'
        db.add_column('incomedeclaration_declarationbiography', 'work_contact_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationBiography.work_contact_ka'
        db.add_column('incomedeclaration_declarationbiography', 'work_contact_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationBiography.place_dob_en'
        db.add_column('incomedeclaration_declarationbiography', 'place_dob_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationBiography.place_dob_ka'
        db.add_column('incomedeclaration_declarationbiography', 'place_dob_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationContract.name_en'
        db.add_column('incomedeclaration_declarationcontract', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationContract.name_ka'
        db.add_column('incomedeclaration_declarationcontract', 'name_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationContract.desc_value_en'
        db.add_column('incomedeclaration_declarationcontract', 'desc_value_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationContract.desc_value_ka'
        db.add_column('incomedeclaration_declarationcontract', 'desc_value_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationContract.date_period_agency_en'
        db.add_column('incomedeclaration_declarationcontract', 'date_period_agency_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationContract.date_period_agency_ka'
        db.add_column('incomedeclaration_declarationcontract', 'date_period_agency_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationContract.financial_result_en'
        db.add_column('incomedeclaration_declarationcontract', 'financial_result_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationContract.financial_result_ka'
        db.add_column('incomedeclaration_declarationcontract', 'financial_result_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationRealEstate.name_shares_en'
        db.add_column('incomedeclaration_declarationrealestate', 'name_shares_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationRealEstate.name_shares_ka'
        db.add_column('incomedeclaration_declarationrealestate', 'name_shares_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationRealEstate.prop_type_en'
        db.add_column('incomedeclaration_declarationrealestate', 'prop_type_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationRealEstate.prop_type_ka'
        db.add_column('incomedeclaration_declarationrealestate', 'prop_type_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationRealEstate.loc_area_en'
        db.add_column('incomedeclaration_declarationrealestate', 'loc_area_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationRealEstate.loc_area_ka'
        db.add_column('incomedeclaration_declarationrealestate', 'loc_area_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationRealEstate.co_owners_en'
        db.add_column('incomedeclaration_declarationrealestate', 'co_owners_en',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationRealEstate.co_owners_ka'
        db.add_column('incomedeclaration_declarationrealestate', 'co_owners_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationCash.name_en'
        db.add_column('incomedeclaration_declarationcash', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationCash.name_ka'
        db.add_column('incomedeclaration_declarationcash', 'name_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationCash.amt_currency_en'
        db.add_column('incomedeclaration_declarationcash', 'amt_currency_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationCash.amt_currency_ka'
        db.add_column('incomedeclaration_declarationcash', 'amt_currency_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationWage.name_en'
        db.add_column('incomedeclaration_declarationwage', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationWage.name_ka'
        db.add_column('incomedeclaration_declarationwage', 'name_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationWage.desc_workplace_en'
        db.add_column('incomedeclaration_declarationwage', 'desc_workplace_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationWage.desc_workplace_ka'
        db.add_column('incomedeclaration_declarationwage', 'desc_workplace_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationWage.desc_job_en'
        db.add_column('incomedeclaration_declarationwage', 'desc_job_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationWage.desc_job_ka'
        db.add_column('incomedeclaration_declarationwage', 'desc_job_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationWage.income_rec_en'
        db.add_column('incomedeclaration_declarationwage', 'income_rec_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationWage.income_rec_ka'
        db.add_column('incomedeclaration_declarationwage', 'income_rec_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationOtherInclExpense.recip_issuer_en'
        db.add_column('incomedeclaration_declarationotherinclexpense', 'recip_issuer_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationOtherInclExpense.recip_issuer_ka'
        db.add_column('incomedeclaration_declarationotherinclexpense', 'recip_issuer_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationOtherInclExpense.type_en'
        db.add_column('incomedeclaration_declarationotherinclexpense', 'type_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationOtherInclExpense.type_ka'
        db.add_column('incomedeclaration_declarationotherinclexpense', 'type_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationOtherInclExpense.amount_en'
        db.add_column('incomedeclaration_declarationotherinclexpense', 'amount_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationOtherInclExpense.amount_ka'
        db.add_column('incomedeclaration_declarationotherinclexpense', 'amount_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IncomeDeclaration.name_en'
        db.add_column('incomedeclaration_incomedeclaration', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IncomeDeclaration.name_ka'
        db.add_column('incomedeclaration_incomedeclaration', 'name_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationSecurity.name_en'
        db.add_column('incomedeclaration_declarationsecurity', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationSecurity.name_ka'
        db.add_column('incomedeclaration_declarationsecurity', 'name_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationSecurity.issuer_en'
        db.add_column('incomedeclaration_declarationsecurity', 'issuer_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationSecurity.issuer_ka'
        db.add_column('incomedeclaration_declarationsecurity', 'issuer_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationSecurity.type_en'
        db.add_column('incomedeclaration_declarationsecurity', 'type_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationSecurity.type_ka'
        db.add_column('incomedeclaration_declarationsecurity', 'type_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationSecurity.price_en'
        db.add_column('incomedeclaration_declarationsecurity', 'price_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationSecurity.price_ka'
        db.add_column('incomedeclaration_declarationsecurity', 'price_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationDeposit.name_en'
        db.add_column('incomedeclaration_declarationdeposit', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationDeposit.name_ka'
        db.add_column('incomedeclaration_declarationdeposit', 'name_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationDeposit.bank_en'
        db.add_column('incomedeclaration_declarationdeposit', 'bank_en',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationDeposit.bank_ka'
        db.add_column('incomedeclaration_declarationdeposit', 'bank_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationDeposit.type_en'
        db.add_column('incomedeclaration_declarationdeposit', 'type_en',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationDeposit.type_ka'
        db.add_column('incomedeclaration_declarationdeposit', 'type_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationDeposit.balance_en'
        db.add_column('incomedeclaration_declarationdeposit', 'balance_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DeclarationDeposit.balance_ka'
        db.add_column('incomedeclaration_declarationdeposit', 'balance_ka',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DeclarationGift.name_en'
        db.delete_column('incomedeclaration_declarationgift', 'name_en')

        # Deleting field 'DeclarationGift.name_ka'
        db.delete_column('incomedeclaration_declarationgift', 'name_ka')

        # Deleting field 'DeclarationGift.desc_value_en'
        db.delete_column('incomedeclaration_declarationgift', 'desc_value_en')

        # Deleting field 'DeclarationGift.desc_value_ka'
        db.delete_column('incomedeclaration_declarationgift', 'desc_value_ka')

        # Deleting field 'DeclarationGift.giver_rel_en'
        db.delete_column('incomedeclaration_declarationgift', 'giver_rel_en')

        # Deleting field 'DeclarationGift.giver_rel_ka'
        db.delete_column('incomedeclaration_declarationgift', 'giver_rel_ka')

        # Deleting field 'DeclarationEntrepreneurial.name_en'
        db.delete_column('incomedeclaration_declarationentrepreneurial', 'name_en')

        # Deleting field 'DeclarationEntrepreneurial.name_ka'
        db.delete_column('incomedeclaration_declarationentrepreneurial', 'name_ka')

        # Deleting field 'DeclarationEntrepreneurial.corp_name_addr_en'
        db.delete_column('incomedeclaration_declarationentrepreneurial', 'corp_name_addr_en')

        # Deleting field 'DeclarationEntrepreneurial.corp_name_addr_ka'
        db.delete_column('incomedeclaration_declarationentrepreneurial', 'corp_name_addr_ka')

        # Deleting field 'DeclarationEntrepreneurial.particn_type_en'
        db.delete_column('incomedeclaration_declarationentrepreneurial', 'particn_type_en')

        # Deleting field 'DeclarationEntrepreneurial.particn_type_ka'
        db.delete_column('incomedeclaration_declarationentrepreneurial', 'particn_type_ka')

        # Deleting field 'DeclarationEntrepreneurial.register_agency_en'
        db.delete_column('incomedeclaration_declarationentrepreneurial', 'register_agency_en')

        # Deleting field 'DeclarationEntrepreneurial.register_agency_ka'
        db.delete_column('incomedeclaration_declarationentrepreneurial', 'register_agency_ka')

        # Deleting field 'DeclarationEntrepreneurial.particn_date_en'
        db.delete_column('incomedeclaration_declarationentrepreneurial', 'particn_date_en')

        # Deleting field 'DeclarationEntrepreneurial.particn_date_ka'
        db.delete_column('incomedeclaration_declarationentrepreneurial', 'particn_date_ka')

        # Deleting field 'DeclarationEntrepreneurial.income_rec_en'
        db.delete_column('incomedeclaration_declarationentrepreneurial', 'income_rec_en')

        # Deleting field 'DeclarationEntrepreneurial.income_rec_ka'
        db.delete_column('incomedeclaration_declarationentrepreneurial', 'income_rec_ka')

        # Deleting field 'DeclarationFamily.name_en'
        db.delete_column('incomedeclaration_declarationfamily', 'name_en')

        # Deleting field 'DeclarationFamily.name_ka'
        db.delete_column('incomedeclaration_declarationfamily', 'name_ka')

        # Deleting field 'DeclarationFamily.surname_en'
        db.delete_column('incomedeclaration_declarationfamily', 'surname_en')

        # Deleting field 'DeclarationFamily.surname_ka'
        db.delete_column('incomedeclaration_declarationfamily', 'surname_ka')

        # Deleting field 'DeclarationFamily.pob_en'
        db.delete_column('incomedeclaration_declarationfamily', 'pob_en')

        # Deleting field 'DeclarationFamily.pob_ka'
        db.delete_column('incomedeclaration_declarationfamily', 'pob_ka')

        # Deleting field 'DeclarationFamily.dob_en'
        db.delete_column('incomedeclaration_declarationfamily', 'dob_en')

        # Deleting field 'DeclarationFamily.dob_ka'
        db.delete_column('incomedeclaration_declarationfamily', 'dob_ka')

        # Deleting field 'DeclarationFamily.relation_en'
        db.delete_column('incomedeclaration_declarationfamily', 'relation_en')

        # Deleting field 'DeclarationFamily.relation_ka'
        db.delete_column('incomedeclaration_declarationfamily', 'relation_ka')

        # Deleting field 'DeclarationProperty.name_shares_en'
        db.delete_column('incomedeclaration_declarationproperty', 'name_shares_en')

        # Deleting field 'DeclarationProperty.name_shares_ka'
        db.delete_column('incomedeclaration_declarationproperty', 'name_shares_ka')

        # Deleting field 'DeclarationProperty.prop_type_en'
        db.delete_column('incomedeclaration_declarationproperty', 'prop_type_en')

        # Deleting field 'DeclarationProperty.prop_type_ka'
        db.delete_column('incomedeclaration_declarationproperty', 'prop_type_ka')

        # Deleting field 'DeclarationProperty.description_en'
        db.delete_column('incomedeclaration_declarationproperty', 'description_en')

        # Deleting field 'DeclarationProperty.description_ka'
        db.delete_column('incomedeclaration_declarationproperty', 'description_ka')

        # Deleting field 'DeclarationProperty.co_owners_en'
        db.delete_column('incomedeclaration_declarationproperty', 'co_owners_en')

        # Deleting field 'DeclarationProperty.co_owners_ka'
        db.delete_column('incomedeclaration_declarationproperty', 'co_owners_ka')

        # Deleting field 'DeclarationBiography.position_en'
        db.delete_column('incomedeclaration_declarationbiography', 'position_en')

        # Deleting field 'DeclarationBiography.position_ka'
        db.delete_column('incomedeclaration_declarationbiography', 'position_ka')

        # Deleting field 'DeclarationBiography.work_contact_en'
        db.delete_column('incomedeclaration_declarationbiography', 'work_contact_en')

        # Deleting field 'DeclarationBiography.work_contact_ka'
        db.delete_column('incomedeclaration_declarationbiography', 'work_contact_ka')

        # Deleting field 'DeclarationBiography.place_dob_en'
        db.delete_column('incomedeclaration_declarationbiography', 'place_dob_en')

        # Deleting field 'DeclarationBiography.place_dob_ka'
        db.delete_column('incomedeclaration_declarationbiography', 'place_dob_ka')

        # Deleting field 'DeclarationContract.name_en'
        db.delete_column('incomedeclaration_declarationcontract', 'name_en')

        # Deleting field 'DeclarationContract.name_ka'
        db.delete_column('incomedeclaration_declarationcontract', 'name_ka')

        # Deleting field 'DeclarationContract.desc_value_en'
        db.delete_column('incomedeclaration_declarationcontract', 'desc_value_en')

        # Deleting field 'DeclarationContract.desc_value_ka'
        db.delete_column('incomedeclaration_declarationcontract', 'desc_value_ka')

        # Deleting field 'DeclarationContract.date_period_agency_en'
        db.delete_column('incomedeclaration_declarationcontract', 'date_period_agency_en')

        # Deleting field 'DeclarationContract.date_period_agency_ka'
        db.delete_column('incomedeclaration_declarationcontract', 'date_period_agency_ka')

        # Deleting field 'DeclarationContract.financial_result_en'
        db.delete_column('incomedeclaration_declarationcontract', 'financial_result_en')

        # Deleting field 'DeclarationContract.financial_result_ka'
        db.delete_column('incomedeclaration_declarationcontract', 'financial_result_ka')

        # Deleting field 'DeclarationRealEstate.name_shares_en'
        db.delete_column('incomedeclaration_declarationrealestate', 'name_shares_en')

        # Deleting field 'DeclarationRealEstate.name_shares_ka'
        db.delete_column('incomedeclaration_declarationrealestate', 'name_shares_ka')

        # Deleting field 'DeclarationRealEstate.prop_type_en'
        db.delete_column('incomedeclaration_declarationrealestate', 'prop_type_en')

        # Deleting field 'DeclarationRealEstate.prop_type_ka'
        db.delete_column('incomedeclaration_declarationrealestate', 'prop_type_ka')

        # Deleting field 'DeclarationRealEstate.loc_area_en'
        db.delete_column('incomedeclaration_declarationrealestate', 'loc_area_en')

        # Deleting field 'DeclarationRealEstate.loc_area_ka'
        db.delete_column('incomedeclaration_declarationrealestate', 'loc_area_ka')

        # Deleting field 'DeclarationRealEstate.co_owners_en'
        db.delete_column('incomedeclaration_declarationrealestate', 'co_owners_en')

        # Deleting field 'DeclarationRealEstate.co_owners_ka'
        db.delete_column('incomedeclaration_declarationrealestate', 'co_owners_ka')

        # Deleting field 'DeclarationCash.name_en'
        db.delete_column('incomedeclaration_declarationcash', 'name_en')

        # Deleting field 'DeclarationCash.name_ka'
        db.delete_column('incomedeclaration_declarationcash', 'name_ka')

        # Deleting field 'DeclarationCash.amt_currency_en'
        db.delete_column('incomedeclaration_declarationcash', 'amt_currency_en')

        # Deleting field 'DeclarationCash.amt_currency_ka'
        db.delete_column('incomedeclaration_declarationcash', 'amt_currency_ka')

        # Deleting field 'DeclarationWage.name_en'
        db.delete_column('incomedeclaration_declarationwage', 'name_en')

        # Deleting field 'DeclarationWage.name_ka'
        db.delete_column('incomedeclaration_declarationwage', 'name_ka')

        # Deleting field 'DeclarationWage.desc_workplace_en'
        db.delete_column('incomedeclaration_declarationwage', 'desc_workplace_en')

        # Deleting field 'DeclarationWage.desc_workplace_ka'
        db.delete_column('incomedeclaration_declarationwage', 'desc_workplace_ka')

        # Deleting field 'DeclarationWage.desc_job_en'
        db.delete_column('incomedeclaration_declarationwage', 'desc_job_en')

        # Deleting field 'DeclarationWage.desc_job_ka'
        db.delete_column('incomedeclaration_declarationwage', 'desc_job_ka')

        # Deleting field 'DeclarationWage.income_rec_en'
        db.delete_column('incomedeclaration_declarationwage', 'income_rec_en')

        # Deleting field 'DeclarationWage.income_rec_ka'
        db.delete_column('incomedeclaration_declarationwage', 'income_rec_ka')

        # Deleting field 'DeclarationOtherInclExpense.recip_issuer_en'
        db.delete_column('incomedeclaration_declarationotherinclexpense', 'recip_issuer_en')

        # Deleting field 'DeclarationOtherInclExpense.recip_issuer_ka'
        db.delete_column('incomedeclaration_declarationotherinclexpense', 'recip_issuer_ka')

        # Deleting field 'DeclarationOtherInclExpense.type_en'
        db.delete_column('incomedeclaration_declarationotherinclexpense', 'type_en')

        # Deleting field 'DeclarationOtherInclExpense.type_ka'
        db.delete_column('incomedeclaration_declarationotherinclexpense', 'type_ka')

        # Deleting field 'DeclarationOtherInclExpense.amount_en'
        db.delete_column('incomedeclaration_declarationotherinclexpense', 'amount_en')

        # Deleting field 'DeclarationOtherInclExpense.amount_ka'
        db.delete_column('incomedeclaration_declarationotherinclexpense', 'amount_ka')

        # Deleting field 'IncomeDeclaration.name_en'
        db.delete_column('incomedeclaration_incomedeclaration', 'name_en')

        # Deleting field 'IncomeDeclaration.name_ka'
        db.delete_column('incomedeclaration_incomedeclaration', 'name_ka')

        # Deleting field 'DeclarationSecurity.name_en'
        db.delete_column('incomedeclaration_declarationsecurity', 'name_en')

        # Deleting field 'DeclarationSecurity.name_ka'
        db.delete_column('incomedeclaration_declarationsecurity', 'name_ka')

        # Deleting field 'DeclarationSecurity.issuer_en'
        db.delete_column('incomedeclaration_declarationsecurity', 'issuer_en')

        # Deleting field 'DeclarationSecurity.issuer_ka'
        db.delete_column('incomedeclaration_declarationsecurity', 'issuer_ka')

        # Deleting field 'DeclarationSecurity.type_en'
        db.delete_column('incomedeclaration_declarationsecurity', 'type_en')

        # Deleting field 'DeclarationSecurity.type_ka'
        db.delete_column('incomedeclaration_declarationsecurity', 'type_ka')

        # Deleting field 'DeclarationSecurity.price_en'
        db.delete_column('incomedeclaration_declarationsecurity', 'price_en')

        # Deleting field 'DeclarationSecurity.price_ka'
        db.delete_column('incomedeclaration_declarationsecurity', 'price_ka')

        # Deleting field 'DeclarationDeposit.name_en'
        db.delete_column('incomedeclaration_declarationdeposit', 'name_en')

        # Deleting field 'DeclarationDeposit.name_ka'
        db.delete_column('incomedeclaration_declarationdeposit', 'name_ka')

        # Deleting field 'DeclarationDeposit.bank_en'
        db.delete_column('incomedeclaration_declarationdeposit', 'bank_en')

        # Deleting field 'DeclarationDeposit.bank_ka'
        db.delete_column('incomedeclaration_declarationdeposit', 'bank_ka')

        # Deleting field 'DeclarationDeposit.type_en'
        db.delete_column('incomedeclaration_declarationdeposit', 'type_en')

        # Deleting field 'DeclarationDeposit.type_ka'
        db.delete_column('incomedeclaration_declarationdeposit', 'type_ka')

        # Deleting field 'DeclarationDeposit.balance_en'
        db.delete_column('incomedeclaration_declarationdeposit', 'balance_en')

        # Deleting field 'DeclarationDeposit.balance_ka'
        db.delete_column('incomedeclaration_declarationdeposit', 'balance_ka')


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
            'place_dob_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'place_dob_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'position_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'work_contact': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'work_contact_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'work_contact_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationcash': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationCash'},
            'amt_currency': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'amt_currency_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'amt_currency_ka': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cash'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationcontract': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationContract'},
            'date_period_agency': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_period_agency_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_period_agency_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contracts'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'desc_value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'desc_value_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'desc_value_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financial_result': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'financial_result_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'financial_result_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationdeposit': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationDeposit'},
            'balance': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'balance_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'balance_ka': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'bank': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'bank_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'bank_ka': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deposits'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'type_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'type_ka': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationentrepreneurial': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationEntrepreneurial'},
            'corp_name_addr': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'corp_name_addr_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'corp_name_addr_ka': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entrepreneurials'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income_rec': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'income_rec_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'income_rec_ka': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'particn_date': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'particn_date_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'particn_date_ka': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'particn_type': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'particn_type_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'particn_type_ka': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'register_agency': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'register_agency_en': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'register_agency_ka': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationfamily': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationFamily'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'family'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'dob': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'dob_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dob_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pob': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pob_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pob_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'relation': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'relation_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'relation_ka': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'surname_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'surname_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationgift': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationGift'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gifts'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'desc_value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'desc_value_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'desc_value_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'giver_rel': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'giver_rel_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'giver_rel_ka': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationotherinclexpense': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationOtherInclExpense'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'amount_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'amount_ka': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'otherinclexpenses'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recip_issuer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recip_issuer_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'recip_issuer_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationproperty': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationProperty'},
            'co_owners': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'co_owners_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'co_owners_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'properties'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_shares': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_shares_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_shares_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'prop_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prop_type_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'prop_type_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationrealestate': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationRealEstate'},
            'co_owners': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'co_owners_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'co_owners_ka': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'realestates'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loc_area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'loc_area_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'loc_area_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_shares': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_shares_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_shares_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'prop_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prop_type_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'prop_type_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationsecurity': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationSecurity'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'securities'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'issuer_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'issuer_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'price_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'price_ka': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'type_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'type_ka': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationwage': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationWage'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wages'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'desc_job': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'desc_job_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'desc_job_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'desc_workplace': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'desc_workplace_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'desc_workplace_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income_rec': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'income_rec_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'income_rec_ka': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
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
            'scrape_date': ('django.db.models.fields.DateField', [], {})
        },
        'incomedeclaration.incomedeclarationpluginconf': {
            'Meta': {'object_name': 'IncomeDeclarationPluginConf', 'db_table': "'cmsplugin_incomedeclarationpluginconf'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Income Declarations'", 'max_length': '32'})
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
            'is_majoritarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'party': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'party_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'party_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['popit.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pob': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'default': "'n'", 'max_length': '1'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['incomedeclaration']