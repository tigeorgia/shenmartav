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



class Command (BaseCommand):
    """Command to update parliamentarians' attendance record."""
    #: help string
    help = 'Updates parliamentarians\' attendance records.'


    def _set_attendance_group (self, representatives):
        """Sets the attendance group for given representatives.

        It assumes that representatives is sorted by attendance.

        @param representatives: sorted representatives
        @type representatives: [Representative]
        @return representatives: the modified representatives
        @rtype representatives: [Representative]
        """
        len_reps = len(representatives)
        if len_reps < 100:
            self.stdout.write('WARNING: less than 100 representatives (%d), using deciles might be a bad idea!' % len_reps)
        self.stdout.write('Setting attendance group ')

        decile_size = len_reps / 10 + 1 # round up
        decile2group = [0, 1, 1, 2, 2, 2, 2, 3, 3, 4]
        decile = 0
        count = 0
        for r in representatives:
            self.stdout.write('.')
            r.attendance_group = decile2group[decile]
            if count > 0 and count % decile_size == 0:
                decile += 1
            count += 1

        self.stdout.write(' done\n')
        return representatives


    def _set_attendance_record (self):
        """Sets the attendance record for parliamentarians.

        @return: (parliamentarian) representatives, sorted ascending by
                 attendance percentage
        @rtype: [Representative]
        """
        self.stdout.write('Setting attendance record ')
        representatives = Representative.parliament.all()
        percentages = []
        for r in representatives:
            self.stdout.write('.')
            results = VotingRecordResult.objects.filter(representative=r).values('vote')
            total = len(results)
            not_present = 0
            for result in results:
                if result['vote'] == u'არ ესწრებოდა':
                    not_present += 1

            present = total - not_present
            try:
                percentage = (present / float(total)) * 100
            except ZeroDivisionError:
                percentage = 0
            attendance = u'%s/%s (%.1f%%)' % (present, total, percentage)
            r.attendance_record = attendance
            percentages.append(percentage)
        self.stdout.write(' done')

        # zip reps and percentages together, sort by percentages and unzip
        zipped = zip(representatives, percentages)
        zipped.sort(key=lambda data: data[1])
        representatives, percentages = zip(*zipped)

        self.stdout.write('\n')
        return representatives


    @transaction.commit_on_success
    def handle (self, *args, **options):
        """Command handler."""
        representatives = self._set_attendance_record()
        representatives = self._set_attendance_group(representatives)
        for r in representatives:
            self.stdout.write(u'%s: attendance %s, group %d\n' % (
                r.name, r.attendance_record, r.attendance_group))
            r.save()

