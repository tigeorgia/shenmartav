# -*- coding: utf-8 -*-

from haystack.indexes import SearchIndex, CharField
from haystack import site

from .models import Representative
from apps.popit.models import Organisation, Position



class RepresentativeIndex (SearchIndex):
    text = CharField(document=True, use_template=True)
    slug = CharField(model_attr='slug', null=True)
    name = CharField(model_attr='name', null=True)
    description = CharField(model_attr='description', null=True)
    party = CharField(model_attr='party', null=True)
    electoral_district = CharField(model_attr='electoral_district', null=True)
    elected = CharField(model_attr='elected', null=True)
    pob = CharField(model_attr='pob', null=True)
    family_status = CharField(model_attr='family_status', null=True)
    education = CharField(model_attr='education', null=True)
    salary = CharField(model_attr='salary', null=True)
    expenses = CharField(model_attr='expenses', null=True)
    property_assets = CharField(model_attr='property_assets', null=True)
    committee = CharField(model_attr='committee', null=True)
    faction = CharField(model_attr='faction', null=True)
    additional_information = CharField(model_attr='additional_information', null=True)
site.register(Representative, RepresentativeIndex)



class OrganisationIndex (SearchIndex):
    text = CharField(document=True, use_template=True)
    name = CharField(model_attr='name', null=True)
    summary = CharField(model_attr='summary', null=True)
site.register(Organisation, OrganisationIndex)



class PositionIndex (SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title', null=True)
    place = CharField(model_attr='place', null=True)
    note = CharField(model_attr='note', null=True)
site.register(Position, PositionIndex)
