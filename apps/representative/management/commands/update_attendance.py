# vim: set fileencoding=utf-8
# -*- coding: utf-8 -*
"""
Command update_attendance to update parliamentarians' attendence record.

Depends on representative and votingrecord.
"""
__docformat__ = 'epytext en'

from django.core.management.base import BaseCommand
from django.db import transaction

from representative.models import Representative
from votingrecord.models import VotingRecordResult


#: % threshold when an attendance record is considered suspiciously low
THRESHOLD = 10


class Command (BaseCommand):
    """Command to update parliamentarians' attendance record."""
    #: help string
    help = 'Updates parliamentarians\' attendance records.'


    @transaction.commit_on_success
    def handle (self, *args, **options):
        """Command handler."""
        for representative in Representative.objects.all():
            self.stdout.write('%s: ' % representative.name)
            results = VotingRecordResult.objects.filter(representative=representative)
            total = len(results)
            not_present = 0
            for r in results:
                if r.vote == u'არ ესწრებოდა':
                    not_present += 1

            present = total - not_present
            try:
                percentage = (present / float(total)) * 100
            except ZeroDivisionError:
                percentage = 0
            attendance = '%s/%s (%.1f%%)' % (present, total, percentage)
            representative.attendance_record = attendance

            if percentage < THRESHOLD:
                attendance += ' VERY LOW'
            self.stdout.write(attendance + '\n')

            representative.save()
