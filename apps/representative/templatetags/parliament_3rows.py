from django import template
from apps.representative.models import *

register = template.Library()

def get_members():
    """Get members of this unit.

    @return: members of this unit
    @rtype: [ representative.Representative ]
    """
    try:
        unit = Unit.objects.get(short="parliament")
    except Unit.DoesNotExist:
        return []

    try:
        members = unit.active_term.representatives.all()
    except AttributeError:
        return []

    members = Representative.by_lastname_firstname_first(members)
    for member in members:
        """
        Avoid a browser bug with names longer than available width making
        member boxes in the unit of the find page jump up a few pixels.
        You probably need to apply the template tag filter 'linebreaksbr' when
        using this.
        Note the replacement only done once - the box starts jumping again
        if there are three parts seperated by the linebreak *sigh*
        """
        if member['firstname_first'] is None:
            member['name'] = ''
        else:
            member['name'] = member['firstname_first'].replace(' ', '\n', 1)
    return members



@register.inclusion_tag('representative/parl_row_li.html')
def get_mprow_of3(row_num):
    result = []
    allmps = get_members()
    for i in range(row_num,len(allmps),3):
        result.append(allmps[i])
    return {'members': result}
