# vim: set fileencoding=utf-8
# -*- coding: utf-8 -*
"""
Command update_attendance to update parliamentarians' attendence record.

Depends on representative and votingrecord.
"""
__docformat__ = 'epytext en'

from django.core.management.base import BaseCommand
from django.db import transaction

from representative.models import Attendance, Representative
from votingrecord.models import VotingRecordResult



class Command (BaseCommand):
    """Command to update parliamentarians' attendance record."""
    #: help string
    help = 'Updates parliamentarians\' attendance records.'


    def _set_groups (self):
        """Sets the attendance groups for parliamentarians."""
        representatives = Representative.parliament.all()
        len_reps = len(representatives)
        if len_reps < 100:
            self.stdout.write('WARNING: less than 100 representatives (%d), using deciles might be a bad idea!' % len_reps)
        self.stdout.write('Setting attendance groups ')

        decile_size = len_reps / 10 + 1 # round up
        decile2group = [0, 1, 1, 2, 2, 2, 2, 3, 3, 4]
        decile = 0
        count = 0
        attendances = Attendance.objects.filter(
            representative__in=representatives).order_by('attended')
        for a in attendances:
            self.stdout.write('.')
            a.group = decile2group[decile]
            a.save()
            if count > 0 and count % decile_size == 0:
                decile += 1
            count += 1

        self.stdout.write(' done\n')
        return attendances


    def _set_attendances (self):
        """Sets the attendance records for parliamentarians."""
        self.stdout.write('Setting attendance records ')
        representatives = Representative.parliament.all()
        for r in representatives:
            self.stdout.write('.')
            try:
                attendance = Attendance.objects.get(representative=r)
            except Attendance.DoesNotExist:
                attendance = Attendance()
                attendance.representative = r

            absent = 0
            attended = 0
            results = VotingRecordResult.objects.filter(representative=r).values('vote')
            for result in results:
                if result['vote'] == u'არ ესწრებოდა':
                    absent += 1
                else:
                    attended += 1
            attendance.attended = attended
            attendance.absent = absent
            attendance.total = attended + absent

            try:
                percentage = (attended / float(attendance.total)) * 100.
            except ZeroDivisionError:
                percentage = 0
            attendance.percentage_attended = percentage
            attendance.percentage_absent = 100. - percentage

            attendance.save()
        self.stdout.write(' done\n')


    @transaction.commit_on_success
    def handle (self, *args, **options):
        """Command handler."""
        self._set_attendances()
        attendances = self._set_groups()
        for a in attendances:
            self.stdout.write(u'%s, %d group %d\n' % (a, a.representative.pk, a.group))
