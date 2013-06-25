from django import template
from apps.representative.views import UnitParliament

register = template.Library()

@register.inclusion_tag('representative/parl_row_li.html')
def get_mprow_of3(row_num):
    unit = UnitParliament()
    result = []
    allmps = unit._get_members()
    for i in range(row_num,len(allmps),3):
        result.append(allmps[i])
    return {'members': result}
