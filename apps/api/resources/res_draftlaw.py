"""
Resources draftlaw
"""
__docformat__ = 'epytext en'

from tastypie import fields

from draftlaw.models import DraftLaw, DraftLawDiscussion, DraftLawChild
from .common import CommonModelResource



class DraftLawDiscussionResource (CommonModelResource):
    draftlaw = fields.ToOneField('api.resources.res_draftlaw.DraftLawResource', 'draftlaw')

    class Meta:
        queryset = DraftLawDiscussion.objects.all()



class DraftLawChildResource (CommonModelResource):
    parent = fields.ToOneField('api.resources.DraftLawResource', 'parent')

    class Meta:
        queryset = DraftLawChild.objects.all()


class DraftLawResource (CommonModelResource):
    discussions = fields.ToManyField(DraftLawDiscussionResource, 'discussions', full=True)
    children = fields.ToManyField(DraftLawChildResource, 'children', full=True)

    class Meta:
        queryset = DraftLaw.objects.all()
