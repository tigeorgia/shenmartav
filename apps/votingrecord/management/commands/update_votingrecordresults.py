# -*- coding: utf-8 -*
"""
Command update_votingrecordresults to update results of voting records with
foreign keys to representatives and CSS class.

Depends on representative.
"""
__docformat__ = 'epytext en'

from django.core.management.base import BaseCommand
from django.db import transaction

from apps.representative.models import Representative
from apps.votingrecord.models import VotingRecordResult

class Command (BaseCommand):
    """Command to update votingrecord results."""
    #: help string
    help = 'Updates votingrecord results: representative and css.'


    @transaction.commit_on_success
    def handle (self, *args, **options):
        """Command handler."""

        representatives = {}
        for r in VotingRecordResult.objects.all():
            out = ['Result for %s' % r.record.number.encode('utf-8')]

            if r.name in representatives:
                r.representative = representatives[r.name]
            else:
                r.representative = Representative.find(r.name)
                if r.representative:
                    representatives[r.name] = r.representative

            if r.representative:
                out.append(' got representative %s' % r.name.encode('utf-8'))

            if r.vote == u'დიახ':
                r.css = 'vote-yes'
            elif r.vote == u'არა':
                r.css = 'vote-no'
            elif r.vote == u'არ მიუცია':
                r.css = 'vote-abstention'
            else:
                r.css = 'vote-absent'
            out.append(' css %s' % r.css)

            r.save()
            self.stdout.write(''.join(out) + '\n')

