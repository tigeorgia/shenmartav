"""
Resources representative
"""
__docformat__ = 'epytext en'

from tastypie import fields

from representative.models import Representative, AdditionalInformation
from popit.api import PositionResource, PersonNameResource
from .common import CommonModelResource



class AdditionalInformationResource (CommonModelResource):
    representative = fields.ToOneField('api.resources.res_representative.RepresentativeResource', 'representative')

    class Meta:
        queryset = AdditionalInformation.objects.all()



class RepresentativeResource (CommonModelResource):
    additional_information = fields.ToManyField(AdditionalInformationResource, 'additional_information', full=True)
    position = fields.ToManyField(PositionResource, 'position_set', related_name='representative', full=True)
    names = fields.ToManyField(PersonNameResource, 'names', full=True)

    class Meta:
        queryset = Representative.objects.all()
        resource_name = 'representative'
