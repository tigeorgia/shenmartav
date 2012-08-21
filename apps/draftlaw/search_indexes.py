"""
Search indexes draftlaw
"""
__docformat__ = 'epytext en'

import datetime
from haystack.indexes import SearchIndex, CharField
from haystack import site

from .models import DraftLaw



class DraftLawIndex (SearchIndex):
    text = CharField(document=True, use_template=True)
    bill_number = CharField(model_attr='bill_number', null=True)
    title = CharField(model_attr='title', null=True)
    initiator = CharField(model_attr='initiator', null=True)
    author = CharField(model_attr='author', null=True)
    status = CharField(model_attr='status', null=True)
    summary = CharField(model_attr='summary', null=True)
    full_text = CharField(model_attr='full_text', null=True)
    full_text_url = CharField(model_attr='full_text_url', null=True)
    enacted_text_url = CharField(model_attr='enacted_text_url', null=True)
    law_number = CharField(model_attr='law_number', null=True)
site.register(DraftLaw, DraftLawIndex)
