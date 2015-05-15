# -*- coding: utf-8 -*-

"""
URLs api
"""
__docformat__ = 'epytext en'

from django.conf.urls.defaults import patterns, include, url

from tastypie.api import Api
v1_api = Api(api_name='v1')

from .resources.res_representative import RepresentativeResource
v1_api.register(RepresentativeResource())

from .resources.res_draftlaw import DraftLawResource
v1_api.register(DraftLawResource())

from .resources.res_incomedeclaration import IncomeDeclarationResource
v1_api.register(IncomeDeclarationResource())

from .resources.res_votingrecord import VotingRecordResource, VotingRecordDetailResource
v1_api.register(VotingRecordResource())
v1_api.register(VotingRecordDetailResource())

from .resources.res_question import QuestionResource
v1_api.register(QuestionResource())

from .resources.res_blog import BlogResource
v1_api.register(BlogResource())

from .resources.res_smsregister import SMSRegisterResource
v1_api.register(SMSRegisterResource())

urlpatterns = patterns('',
    url(r'', include(v1_api.urls)),
)
