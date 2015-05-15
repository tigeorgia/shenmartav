# -*- coding: utf-8 -*-


"""
Command to update draft laws with voting records
"""
__docformat__ = 'epytext en'

from django.core.management.base import BaseCommand
from django.db import transaction

from draftlaw.models import DraftLaw, DraftLawChild
from votingrecord.models import VotingRecord



class Command (BaseCommand):
    """Command to update draft laws with voting records."""
    #: help string
    help = 'Update draft law records with voting records.'


    def _get_voting_record (self, law_number):
        """Get voting record for given law number.

        @param law_number: law number to find voting record for
        @type law_number: str
        @return: voting record
        @rtype: votingrecord.VotingRecord
        """
        if not law_number:
            return None

        try:
            vr = VotingRecord.objects.filter(number=law_number)
            return vr[0] # shouldn't be more than one with same number...
        except IndexError:
            return None


    @transaction.commit_on_success
    def _handle_object (self, obj):
        """Handle a draft law or draft law child."""
        self.stdout.write('%s | %s ... ' % (obj.bill_number, obj.title))
        vr = self._get_voting_record(obj.law_number)
        if vr:
            self.stdout.write('found %s' % obj.law_number)
            obj.voting_record = vr
            obj.save()
        self.stdout.write('\n')


    def handle (self, *args, **options):
        """Command handler."""
        for d in DraftLaw.objects.filter(law_number__isnull=False):
            self._handle_object(d)
        for c in DraftLawChild.objects.filter(law_number__isnull=False):
            self._handle_object(c)
