# -*- coding: utf-8 -*-

"""
Resources incomedeclaration
"""
__docformat__ = 'epytext en'

from tastypie import fields

from votingrecord.models import VotingRecord, VotingRecordResult, VotingRecordAmendment
from .common import CommonModelResource, CommonResource


class VotingRecordResultResource (CommonModelResource):
    class Meta:
        queryset = VotingRecordResult.objects.all()



class VotingRecordAmendmentResource (CommonModelResource):
    class Meta:
        queryset = VotingRecordAmendment.objects.all()



class VotingRecordDetailResource (CommonModelResource):
    results = fields.ToManyField(VotingRecordResultResource, 'results', full=True)
    amendments = fields.ToManyField(VotingRecordAmendmentResource, 'amendments', full=True)

    class Meta:
        queryset = VotingRecord.objects.all()



class VotingRecordResource (CommonResource):
    name = fields.CharField(attribute='name')

    def obj_get_list (self, **kwargs):
        return VotingRecord.objects.all()


    def get_resource_uri (self, bundle):
        kwargs = {
            'resource_name': 'votingrecorddetail',
            'pk': bundle.obj.pk
        }

        if self._meta.api_name is not None:
            kwargs['api_name'] = self._meta.api_name

        return self._build_reverse_url('api_dispatch_detail', kwargs=kwargs)
