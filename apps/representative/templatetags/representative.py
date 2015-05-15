# -*- coding: utf-8 -*-

"""
Representative templatetags
"""
from django import template
from django.utils import dateformat
from django.utils.translation import ugettext_lazy as _

register = template.Library()

@register.filter
def percentage (value, total):
    """Calculate percentage value of given absolutes.

    @param value: absolute value to get percentage for
    @type value: int
    @param total: absolute total
    @type total: int
    """
    if total:
        return '%.1f%%' % (value * 100. / total)
    else:
        return '0%'



@register.filter
def repdate (approx):
    """Alternative to Django's date filter which doesn't play well with ApproximateDateFields.

    @param approx: approximate date
    @type: ApproximateDateField
    @return: nicely formatted date
    @rtype: str
    """
    if not approx:
        return ''

    if approx.month == 1 and approx.day == 1:
        return dateformat.format(approx, 'Y').encode('utf-8')
    elif hasattr(approx, 'future') and approx.future:
        return _(u'future')
    elif approx.year and approx.month and approx.day:
        # return dateformat.format(approx, 'j F Y').encode('utf-8')
        return dateformat.format(approx, 'Y').encode('utf-8')
    elif approx.year and approx.month:
        #return dateformat.format(approx, 'F Y').encode('utf-8')
        return dateformat.format(approx, 'Y').encode('utf-8')
    elif approx.year:
        return dateformat.format(approx, 'Y').encode('utf-8')
    else:
        return _(u'invalid')
