# -*- coding: utf-8 -*-

"""
Resources question
"""
__docformat__ = 'epytext en'

from question.models import Question
from .common import CommonModelResource



class QuestionResource (CommonModelResource):
    class Meta:
        queryset = Question.public
        excludes = ['email', 'mobile', 'is_public']
