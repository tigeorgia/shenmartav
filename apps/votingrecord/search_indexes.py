import datetime
from haystack.indexes import *
from haystack import site
from .models import VotingRecord


class VotingRecordIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    kan_id = CharField(model_attr='kan_id', null=True)
    name = CharField(model_attr='name', null=True)
    date = CharField(model_attr='date', null=True)
    number = CharField(model_attr='number', null=True)

#    def index_queryset(self):
#        """Used when the entire index for model is updated."""
#        return Note.objects.filter(pub_date__lte=datetime.datetime.now())


site.register(VotingRecord, VotingRecordIndex)
