from modeltranslation.translator import translator, TranslationOptions

from apps.incomedeclaration.models import IncomeDeclaration, DeclarationSecurity, \
    DeclarationFamily, DeclarationContract, DeclarationDeposit, \
    DeclarationCash, DeclarationGift, DeclarationEntrepreneurial, \
    DeclarationRealEstate, DeclarationWage, DeclarationProperty, \
    DeclarationOtherInclExpense, DeclarationBiography


class IncomeDeclarationTranslationOptions(TranslationOptions):
    fields = ('name',)


class DeclarationBiographyTranslationOptions(TranslationOptions):
    fields = ('position', 'work_contact', 'place_dob',)


class DeclarationCashTranslationOptions(TranslationOptions):
    fields = ('name', 'amt_currency',)


class DeclarationContractTranslationOptions(TranslationOptions):
    fields = ('name', 'desc_value', 'date_period_agency', 'financial_result',)


class DeclarationDepositTranslationOptions(TranslationOptions):
    fields = ('name', 'bank', 'type', 'balance',)


class DeclarationEntrepreneurialTranslationOptions(TranslationOptions):
    fields = ('name', 'corp_name_addr', 'particn_type', 'register_agency', 'particn_date', 'income_rec',)


class DeclarationFamilyTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'pob', 'dob', 'relation',)


class DeclarationGiftTranslationOptions(TranslationOptions):
    fields = ('name', 'desc_value', 'giver_rel',)


class DeclarationOtherInclExpenseTranslationOptions(TranslationOptions):
    fields = ('recip_issuer', 'type', 'amount',)


class DeclarationPropertyTranslationOptions(TranslationOptions):
    fields = ('name_shares', 'prop_type', 'description', 'co_owners',)


class DeclarationRealEstateTranslationOptions(TranslationOptions):
    fields = ('name_shares', 'prop_type', 'loc_area', 'co_owners',)


class DeclarationSecurityTranslationOptions(TranslationOptions):
    fields = ('name', 'issuer', 'type', 'price', 'quantity',)


class DeclarationWageTranslationOptions(TranslationOptions):
    fields = ('name', 'desc_workplace', 'desc_job', 'income_rec',)


translator.register(IncomeDeclaration, IncomeDeclarationTranslationOptions)
translator.register(DeclarationBiography, DeclarationBiographyTranslationOptions)
translator.register(DeclarationCash, DeclarationCashTranslationOptions)
translator.register(DeclarationContract, DeclarationContractTranslationOptions)
translator.register(DeclarationDeposit, DeclarationDepositTranslationOptions)
translator.register(DeclarationEntrepreneurial, DeclarationEntrepreneurialTranslationOptions)
translator.register(DeclarationFamily, DeclarationFamilyTranslationOptions)
translator.register(DeclarationGift, DeclarationGiftTranslationOptions)
translator.register(DeclarationOtherInclExpense, DeclarationOtherInclExpenseTranslationOptions)
translator.register(DeclarationProperty, DeclarationPropertyTranslationOptions)
translator.register(DeclarationRealEstate, DeclarationRealEstateTranslationOptions)
translator.register(DeclarationSecurity, DeclarationSecurityTranslationOptions)
translator.register(DeclarationWage, DeclarationWageTranslationOptions)
