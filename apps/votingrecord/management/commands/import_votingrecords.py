#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Command import_votingrecord
"""
__docformat__ = 'epytext en'

import json
import re
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from optparse import make_option
import glt

from apps.votingrecord.models import VotingRecord, VotingRecordAmendment, VotingRecordResult


class Command (BaseCommand):
    """Command to import voting records from a JSON file."""
    #: allowed arguments to the command
    args = '<filename filename ...>'
    #: help string
    help = 'Imports a voting record from a JSON file.'
    #: custom options
    option_list = BaseCommand.option_list + (
        make_option(
            '--force',
            action='store_true',
            dest='force',
            default=False,
            help='Force overwriting income declarations even though scrape date is not newer.'
        ),
    )
    #: force overwriting income declarations even though scrape date is not newer
    force = False

    def _get_can_number_and_chars(self, kanstr):
        """
        Get numbers and chars from the kan ID
        @return: Numbers and chars from kan ID
        @rtype: list
        """
        number = re.findall("\d+", kanstr)[0]
        char = kanstr.replace(number, '').replace('-', '')
        return (number.strip(), char.strip())


    def _strip (self, tostrip):
        """Stringstrip the given parameter.

        @param tostrip: 'string' to strip
        @type tostrip: str (hopefully)
        @return: (stripped) parameter.
        @rtype: str (hopefully)
        """
        if tostrip:
            return tostrip.strip().strip(u'“„"')
        else:
            return tostrip



    def _getVoteGeo(self, vote):
      if( vote == "Yes" ):
        return u'დიახ'
      elif( vote == "No" ):
        return u'არა'
      elif( vote == "Abstain" ):
        return u'არ მიუცია'
      elif( vote == "Not Present" ):
        return u'თავი შეიკავა/არ იმყოფებოდა'
      else:
        return 'None'
    
    def _getVoteEng(self, vote):
      if( vote == "Yes" ):
        return u'Yes'
      elif( vote == "No" ):
        return u'No'
      elif( vote == "Abstain" ):
        return u'Abstain'
      elif( vote == "Not Present" ):
        return u'Abstain/Absent'
      else:
        return 'None'

    @transaction.commit_on_success
    def _save_results (self, record, results):
        """Save results for the given record to database.

        @param record: record to save for
        @type record: VotingRecord
        @param results: list of results, vote + name
        @type results: [ {'vote': str, 'name': str} ]
        """
        for result in results:
            vrr = VotingRecordResult(
                record=record,
                vote=self._getVoteGeo(self._strip(result['vote'])),
                vote_ka=self._getVoteGeo(self._strip(result['vote'])),
                vote_en=self._getVoteEng(self._strip(result['vote'])),
                name=self._strip(result['name']),
                session=result['session'],
                totalsession=result['totalsession'])
            vrr.save()


    @transaction.commit_on_success
    def _save_amendments (self, record, amendments):
        """Save amendments for the given record to database.

        @param record: record to save for
        @type record: VotingRecord
        @param amendments: list of bill numbers
        @type amendments: [ str ]
        """

        for amendment in amendments:
            vra = VotingRecordAmendment(
                record=record,
                number=self._strip(amendment))
            vra.save()


    def _exists (self, data, kanID):
        """Check if record to import already exists.

        @param data: record to import.
        @type data: {
            'kan_id': str,
            'scrape_date': str,
            'name': str,
            'date': str,
            'url' : str,
            'number': str,
            'amendmends': [ str ],
            'results': [ {'vote': str, 'name': str} ]
            '}
        @return: if record exists already
        @rtype: bool
        """
        existing = VotingRecord.objects.filter(kan_id=kanID)
        scrape_date = datetime.strptime(data['scrape_date'], '%Y-%m-%d')
        if len(existing) > 0:
            if scrape_date.date() >= existing[0].scrape_date or self.force:
                self.stdout.write('replacing ... ')
                existing[0].delete() # also deletes amendments and results
            else:
                self.stdout.write("already exists, skipping ...\n")
                return True
        else:
            self.stdout.write('new ... ')

        return False

    @transaction.commit_on_success
    def _handle_record (self, filename):
        """Handle a single voting record.

        @param filename: filename of voting record
        @type filename: str
        @return: created voting record object
        @rtype: VotingRecord
        """
        fh = open(filename, 'r')
        data = json.loads( fh.read() )
        fh.close()

        
        unicodeKanId = self._strip( data['kan_id'] ).encode('utf-8')

        self.stdout.write('Importing from %s record %s ... ' % (
            filename, unicodeKanId ))

        print unicodeKanId
        kan_formatted = self._get_can_number_and_chars(unicodeKanId)
        kanId = kan_formatted[0]
        kanIdChar= kan_formatted[1]
        print kanId, kanIdChar
        if self._exists(data,kanId):
            return None

        record = VotingRecord(
            kan_id=kanId,
            kan_id_chars=kanIdChar,
            scrape_date=self._strip(data['scrape_date']),
            name=self._strip(data['name']),
            date=self._strip(data['date'][0:10]),
            url=self._strip(data['url']),
            number=self._strip(data['number']))
        record.save() 


        if data['result']:
            self._save_results(record, data['result'])

        if data['amendments']:
            self._save_amendments(record, data['amendments'])

        self.stdout.write("success!\n")
        return record

    @transaction.commit_on_success
    def _setup_amendments (self):
        """Establish amendment relationships between voting records.

        Only after all records with their string representation of the
        relationship have been imported, we can setup their relationships
        on a database level.
        """
        for record in VotingRecord.objects.all():
            if not record.number: # skip if record has no bill number
                continue

            self.stdout.write('Setup amendments %s: ' % (record.number).encode('utf-8'))
            for amend in record.amendments.all():
                if not amend.number: # don't add amendments with no number
                    continue

                rec = VotingRecord.objects.filter(number=amend.number)
                if len(rec) == 0:
                    rec = VotingRecord(number=amend.number)
                    rec.save()
                else:
                    rec = rec[0] # ignore multiple occurrences

                record.amended_by.add(rec) # won't add dupes
                self.stdout.write('%s ' % amend.number)

            record.save()
            self.stdout.write("done!\n")


    def handle (self, *args, **options):
        """Command handler."""
        if options.get('force'):
            self.force = True
        else:
            self.force = False

        for filename in args:
            self._handle_record(filename)

        self._setup_amendments()

