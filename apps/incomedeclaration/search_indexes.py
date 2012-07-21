import datetime
from haystack.indexes import SearchIndex, CharField
from haystack import site

from .models import IncomeDeclaration


class IncomeDeclarationIndex (SearchIndex):
    text = CharField(document=True, use_template=True)
    decl_id = CharField(model_attr='decl_id', null=True)
    name = CharField(model_attr='name', null=True)
site.register(IncomeDeclaration, IncomeDeclarationIndex)
