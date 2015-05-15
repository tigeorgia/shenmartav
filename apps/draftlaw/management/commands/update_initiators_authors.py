# -*- coding: utf-8 -*-
"""
Command to link draft laws to representatives in initiator / author fields.
"""
__docformat__ = 'epytext en'

from django.core.management.base import BaseCommand
from django.db import transaction

from draftlaw.models import DraftLaw
from representative.models import Representative



class Command (BaseCommand):
    """Command to link draft laws to representatives in initiator / author fields."""
    #: help string
    help = 'Command to link draft laws to representatives in initiator / author fields.'


    def _get_names (self, data):
        """Extract names from given data string (initiator/author).

        @param data: data which possibly contains names
        @type data: str
        """
        names = data.split('(')[0]
        if names.lower().startswith('mp '):
            names = linked[3:]
        if names.lower().startswith('mps '):
           names = linked[4:]

        splitnames = names.split(',')
        if len(splitnames) == 1:
            splitnames = names.split(';')
        return [n.strip() for n in splitnames]


    def _add_representatives (self, draftlaw, field):
        """Add representatives searching for names in given field.

        @param draftlaw: draftlaw to add to
        @type draftlaw: draftlaw.Draftlaw
        @param field: field to search for names in
        @type field: str
        """
        try:
            names = self._get_names(getattr(draftlaw, field))
        except AttributeError:
            return

        base = field.split('_')[0] # remove language
        try:
            field_representatives = getattr(draftlaw, base + '_representatives')
        except AttributeError:
            return

        for name in names:
            representative = Representative.find(name)
            if representative:
                self.stdout.write(u'\n %s: %s' % (
                    field, str(representative.name)))
                field_representatives.add(representative)


    @transaction.commit_on_success
    def handle (self, *args, **options):
        """Command handler."""
        for d in DraftLaw.objects.all():
            self.stdout.write(u'Draftlaw: %s' % str(d).decode('utf-8'))
            self._add_representatives(d, 'initiator_en')
            self._add_representatives(d, 'initiator_ka')
            self._add_representatives(d, 'author_en')
            self._add_representatives(d, 'author_ka')
            self.stdout.write('\n')
