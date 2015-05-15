# -*- coding: utf-8 -*-

"""
Resources incomedeclaration
"""
__docformat__ = 'epytext en'

from tastypie import fields

from incomedeclaration.models import IncomeDeclaration, DeclarationSecurity,\
    DeclarationFamily, DeclarationContract, DeclarationDeposit,\
    DeclarationCash, DeclarationGift, DeclarationEntrepreneurial,\
    DeclarationRealEstate, DeclarationWage, DeclarationProperty,\
    DeclarationOtherInclExpense, DeclarationBiography
from .common import CommonModelResource



class DeclarationBiographyResource (CommonModelResource):
    declaration = fields.ToOneField('api.resources.res_incomedeclaration.IncomeDeclarationResource', 'declaration')

    class Meta:
        queryset = DeclarationBiography.objects.all()



class DeclarationCashResource (CommonModelResource):
    declaration = fields.ToOneField('api.resources.res_incomedeclaration.IncomeDeclarationResource', 'declaration')

    class Meta:
        queryset = DeclarationCash.objects.all()



class DeclarationContractResource (CommonModelResource):
    declaration = fields.ToOneField('api.resources.res_incomedeclaration.IncomeDeclarationResource', 'declaration')

    class Meta:
        queryset = DeclarationContract.objects.all()



class DeclarationDepositResource (CommonModelResource):
    declaration = fields.ToOneField('api.resources.res_incomedeclaration.IncomeDeclarationResource', 'declaration')

    class Meta:
        queryset = DeclarationDeposit.objects.all()



class DeclarationEntrepreneurialResource (CommonModelResource):
    declaration = fields.ToOneField('api.resources.res_incomedeclaration.IncomeDeclarationResource', 'declaration')

    class Meta:
        queryset = DeclarationEntrepreneurial.objects.all()



class DeclarationFamilyResource (CommonModelResource):
    declaration = fields.ToOneField('api.resources.res_incomedeclaration.IncomeDeclarationResource', 'declaration')

    class Meta:
        queryset = DeclarationFamily.objects.all()



class DeclarationGiftResource (CommonModelResource):
    declaration = fields.ToOneField('api.resources.res_incomedeclaration.IncomeDeclarationResource', 'declaration')

    class Meta:
        queryset = DeclarationGift.objects.all()



class DeclarationOtherInclExpenseResource (CommonModelResource):
    declaration = fields.ToOneField('api.resources.res_incomedeclaration.IncomeDeclarationResource', 'declaration')

    class Meta:
        queryset = DeclarationOtherInclExpense.objects.all()



class DeclarationPropertyResource (CommonModelResource):
    declaration = fields.ToOneField('api.resources.res_incomedeclaration.IncomeDeclarationResource', 'declaration')

    class Meta:
        queryset = DeclarationProperty.objects.all()



class DeclarationRealEstateResource (CommonModelResource):
    declaration = fields.ToOneField('api.resources.res_incomedeclaration.IncomeDeclarationResource', 'declaration')

    class Meta:
        queryset = DeclarationRealEstate.objects.all()



class DeclarationSecurityResource (CommonModelResource):
    declaration = fields.ToOneField('api.resources.res_incomedeclaration.IncomeDeclarationResource', 'declaration')

    class Meta:
        queryset = DeclarationSecurity.objects.all()



class DeclarationWageResource (CommonModelResource):
    declaration = fields.ToOneField('api.resources.res_incomedeclaration.IncomeDeclarationResource', 'declaration')

    class Meta:
        queryset = DeclarationWage.objects.all()



class IncomeDeclarationResource (CommonModelResource):
    biographies = fields.ToManyField(DeclarationBiographyResource, 'biographies', full=True)
    cash = fields.ToManyField(DeclarationCashResource, 'cash', full=True)
    contracts = fields.ToManyField(DeclarationContractResource, 'contracts', full=True)
    deposits = fields.ToManyField(DeclarationDepositResource, 'deposits', full=True)
    entrepreneurial = fields.ToManyField(DeclarationEntrepreneurialResource, 'entrepreneurials', full=True)
    family = fields.ToManyField(DeclarationFamilyResource, 'family', full=True)
    gifts = fields.ToManyField(DeclarationGiftResource, 'gifts', full=True)
    otherinclexpenses = fields.ToManyField(DeclarationOtherInclExpenseResource, 'otherinclexpenses', full=True)
    properties = fields.ToManyField(DeclarationPropertyResource, 'properties', full=True)
    realestates = fields.ToManyField(DeclarationRealEstateResource, 'realestates', full=True)
    securities = fields.ToManyField(DeclarationSecurityResource, 'securities', full=True)
    wages = fields.ToManyField(DeclarationWageResource, 'wages', full=True)

    class Meta:
        queryset = IncomeDeclaration.objects.all()
