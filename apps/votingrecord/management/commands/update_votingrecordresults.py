# -*- coding: utf-8 -*
"""
Command update_votingrecordresults to update results of voting records with
foreign keys to representatives and CSS class.

Depends on representative.
"""
__docformat__ = 'epytext en'

import gc
import codecs
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

        number_of_votingrecordresults = VotingRecordResult.objects.count()
        memory_qs = (self._votingrecordresults_qs_iterate(VotingRecordResult.objects.all()))

        with codecs.open('problematic_results.csv', 'w', 'utf-8-sig') as file:
                    file.write('name,record_id\n')

        for item, r in memory_qs:
            name_encoded = r.name.encode('utf-8')
            record_number_encoded = r.record.number.encode('utf-8')

            done = item / number_of_votingrecordresults * 100
            done = int(done * 100) / 100.0
            out = 'Done: {0}%. Result for {1}'.format(done, record_number_encoded)

            r.representative = Representative.find(r.name)

            if r.representative:
                out += ' got representative {0}'.format(name_encoded)
            else:
                out += ' got problematic record: name: {0}, record: {1}'.format(name_encoded, r.record_id)
                with codecs.open('problematic_results.csv', 'a', 'utf-8-sig') as file:
                    file.write(u''.join(r.name) + ',' + str(r.record_id) + '\n')

            if r.vote == u'დიახ':
                r.css = 'vote-yes'
            elif r.vote == u'არა':
                r.css = 'vote-no'
            elif r.vote == u'არ მიუცია':
                r.css = 'vote-abstention'
            else:
                r.css = 'vote-absent'
            out += ' css %s' % r.css

            r.save()
            self.stdout.write(''.join(out) + '\n')

    """
    This should solve huge memory usage with big votingrecordresults table
    """
    def _votingrecordresults_qs_iterate(self, queryset, chunck=800):
        item = 0.0
        id = 0
        last_id = queryset.order_by('-id')[0].id
        queryset = queryset.order_by('id')

        while id < last_id:
            for row in queryset.filter(id__gt=id)[:chunck]:
                item += 1
                id = row.id
                yield item, row
            gc.collect()
