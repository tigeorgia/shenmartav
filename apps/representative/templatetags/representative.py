"""
Representative templatetags
"""
from django import template

register = template.Library()

@register.filter
def percentage (value, total):
    """Calculate percentage value of given absolutes.

    @param value: absolute value to get percentage for
    @type value: int
    @param total: absolute total
    @type total: int
    """
    print 'percentage', value, total
    if total:
        return '%.1f%%' % (value * 100. / total)
    else:
        return '0%'
