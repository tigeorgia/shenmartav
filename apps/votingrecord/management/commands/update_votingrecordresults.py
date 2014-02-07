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
    """Command to update voting record results."""
    help = 'Updates voting record results: representative and css.'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.votingrecords = VotingRecordResult.objects.all()
        self.votingrecords_count = self.votingrecords.count()

    @transaction.commit_on_success
    def handle(self, *args, **options):
        """
        Command handler.
        @param args:
        @param options:
        @return:
        """

        memory_qs = (self._voting_record_results_qs_iterate())

        with codecs.open('problematic_results.csv', 'w', 'utf-8-sig') as f:
                    f.write('name,record_id\n')

        for item, result in memory_qs:
            name_encoded = result.name.encode('utf-8')
            record_number_encoded = result.record.number.encode('utf-8')

            done = item / self.votingrecords_count * 100
            done = int(done * 100) / 100.0
            out = 'Done: {0}%. Result for {1}'.format(done, record_number_encoded)

            result.representative = Representative.find(result.name, 'lastname')

            if result.representative:
                out += ' got representative {0}'.format(name_encoded)
            else:
                out += ' got problematic record: name: {0}, record: {1}'.format(name_encoded, result.record_id)
                with codecs.open('problematic_results.csv', 'a', 'utf-8-sig') as f:
                    f.write(u''.join(result.name) + ',' + str(result.record_id) + '\n')

            if result.vote == u'დიახ':
                result.css = 'vote-yes'
            elif result.vote == u'არა':
                result.css = 'vote-no'
            elif result.vote == u'არ მიუცია':
                result.css = 'vote-abstention'
            else:
                result.css = 'vote-absent'
            out += ' css %s' % result.css

            result.save()
            self.stdout.write(''.join(out) + '\n')

    def _voting_record_results_qs_iterate(self, chunck=800):
        """ This should solve huge memory usage with big votingrecordresults table
        @param chunck: number of records to process before garbage collecting
        @return: generator
        """
        item = 0.0
        cur_id = 0
        last_id = self.votingrecords.order_by('-id')[0].id
        queryset = self.votingrecords.order_by('id')

        while cur_id < last_id:
            for row in queryset.filter(id__gt=cur_id)[:chunck]:
                item += 1
                cur_id = row.id
                yield item, row
            gc.collect()
