import datetime
from haystack.indexes import SearchIndex, CharField
from haystack import site

from .models import VotingRecord


class VotingRecordIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    kan_id = CharField(model_attr='kan_id', null=True)
    name = CharField(model_attr='name', null=True)
    date = CharField(model_attr='date', null=True)
    number = CharField(model_attr='number', null=True)
site.register(VotingRecord, VotingRecordIndex)
