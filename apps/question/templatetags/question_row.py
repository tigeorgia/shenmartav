# -*- coding: utf-8 -*-

from django import template
from apps.question.models import *

register = template.Library()

@register.inclusion_tag('question/question_row.html')
def get_three_questions():
    three_questions = Question.answered.order_by('-date')[:3]
    return {'questions': three_questions}


