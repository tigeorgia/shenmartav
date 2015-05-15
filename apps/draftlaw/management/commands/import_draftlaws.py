# -*- coding: utf-8 -*-

"""
Command to import draft laws as provided by TIG
"""
__docformat__ = 'epytext en'

import csv
import re
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import ugettext as _
from optparse import make_option


#: CSV delimiter
DELIMITER = ','
COL_EN = 18
COL_KA = 9



class Command (BaseCommand):
    """Command to import draftlaws from a CSV file."""
    #: allowed arguments to the command
    args = '<filename>'
    #: help string
    help = 'Imports draftlaw records from a CSV file.'
    #: custom options
    option_list = BaseCommand.option_list + (
        make_option(
            '--force',
            action='store_true',
            dest='force',
            default=False,
            help='Force replacing draftlaws.'
        ),
    )
    #: force overwriting income declarations even though scrape date is not newer
    force = False


    def _get_isodate(self, date):
        """Convert given date to a database-compatible ISO date.

        @param date: date to convert
        @type date: str
        @return: date in ISO format
        @rtype: str
        """
        default = '1970-01-01'
        fmt = '\nWrong date format: %s\n'
        parts = date.strip().split('.')

        if len(parts) != 3:
            self.stdout.write(fmt % date)
            return default

        if len(parts[2]) == 2: # assume '20' missing
            parts[2] = '20' + parts[2]

        if len(parts[2]) != 4 or len(parts[1]) != 2 or len(parts[0]) != 2:
            self.stdout.write(fmt % date)
            return default

        try:
            return '%s-%s-%s' % (parts[2], parts[1], parts[0])
        except IndexError:
            self.stdout.write(fmt % date)
            return default



    @transaction.commit_on_success
    def _add_discussions (self, row, draftlaw):
        """Add discussion to a draftlaw record.

        @param row: data row
        @type row: [ str ]
        @param draftlaw: a draftlaw
        @type draftlaw: draftlaw.DraftLaw
        """
        from draftlaw.models import DraftLawDiscussion
        col_start = 11
        col_end = 16
        for i in xrange(col_start, col_end + 1):
            if not row[i]: continue

            stage = i - col_start
            stripped = row[i].strip()
            places = stripped.split(';')

            if len(places) > 1: # must be committees
                for j in xrange(len(places)):
                    parts = places[j].strip().split(':')
                    if len(parts) != 2: continue
                    discussion = DraftLawDiscussion(draftlaw=draftlaw,
                        date=self._get_isodate(parts[0]),
                        place_ka=parts[1].strip(),
                        stage=stage)
                    discussion.save()
            else: # plenary or single committee
                regex = re.compile("\(.+\)")
                try:
                    datestr = regex.search(stripped).group()
                except AttributeError:
                    datestr = ""
                date = self._get_isodate(datestr.strip('()'))
                if i in [11, 13, 15]: # comittee
                    place = _('Committee')
                else: # plenary
                    place = _('Plenary')
                discussion = DraftLawDiscussion(
                    draftlaw=draftlaw, date=date, place_ka=place, stage=stage)
                discussion.save()


    def _get_status (self, row):
        """Get short and long status for current row.

        @param row: data row
        @type row: [ str ]
        @return: tuple of short and long status
        @rtype: (str, str)
        """
        status = ''
        shortstatus = 'D'

        if row[16]:
            status = _(u'3rd Plenary ') + row[16].strip().decode('utf-8')
            try:
                if status.lower().index('pass'):
                    shortstatus = 'P'
            except ValueError:
                pass
        elif row[15]:
            status = _(u'3rd Comittee ') + row[15].strip().decode('utf-8')
        elif row[14]:
            status = _(u'2nd Plenary ') + row[14].strip().decode('utf-8')
        elif row[13]:
            status = _(u'2nd Committee ') + row[13].strip().decode('utf-8')
        elif row[12]:
            status = _(u'1st Plenary ') + row[12].strip().decode('utf-8')
        elif row[11]:
            status = _(u'1st Committee ') + row[11].strip().decode('utf-8')

        return (shortstatus, status)


    def _get_law_number (self, col):
        """Get law number from given column.

        @param col: column in row to get data from
        @type col: str
        @return: law number
        @rtype: str
        """
        if not col:
            return None

        number = col.strip().replace(' ', '').decode('utf-8')

        try: # weeding out redundant text
            idx = number.index('№') # not working
            number = number[idx+1:]
        except (ValueError, IndexError):
            pass

        return number


    def _get_bill_number (self, row):
        """Get bill number from given row.

        @param row: data row
        @type row: [ str ]
        @return: bill number
        @rtype: str
        """
        number = row[1].strip().replace('–', '-').replace(' ', '')
        if not number.startswith('#'):
            number = '#' + number
        return number


    @transaction.commit_on_success
    def _create_draftlaw (self, row):
        """Create a complete DraftLaw record.

        @param row: data row
        @type row: [ str ]
        @return: a draftlaw
        @rtype: draftlaw.DraftLaw
        """
        from draftlaw.models import DraftLaw
        bill_number = self._get_bill_number(row)

        title = row[3].strip().decode('utf-8')
        try:
           self.stdout.write('%s | %s ... ' % (bill_number, title))
        except UnicodeEncodeError: # need this for Python 2.6 *sigh*
           self.stdout.write('%s | %s ... ' % (bill_number, title.encode('utf-8')))

        (shortstatus, status) = self._get_status(row)

        law_number = self._get_law_number(row[17])

        draftlaw = DraftLaw(
            bureau_date=self._get_isodate(row[0]),
            bill_number=bill_number,
            title_ka=title,
            initiator_ka=row[4].strip(),
            author_ka=row[5].strip(),
            status_ka=status,
            shortstatus=shortstatus,
            summary_ka=row[6].strip(),
            law_number=law_number,
        )
        draftlaw.save()

        draftlaws = DraftLaw.objects.filter(bill_number=draftlaw.bill_number)
        if len(draftlaws) > 1:
            if self.force:
                draftlaws.exclude(pk=draftlaw.pk).delete()
                self.stdout.write('replace existing!')
            else:
                self.stdout.write('keep already existing!')
                draftlaw.delete()
                return None
        else:
            self.stdout.write('add new!')

        self._add_discussions(row, draftlaw)
        return draftlaw



    @transaction.commit_on_success
    def _create_draftlawchild (self, row, parent):
        """Create a DraftLawChild record.

        @param row: data row
        @type row: [ str ]
        @param parent: parent draft law
        @type parent: draftlaw.DraftLaw
        @return: a draftlaw child
        @rtype: draftlaw.DraftLawChild
        """
        from draftlaw.models import DraftLawChild
        if not parent:
            return False

        bill_number = self._get_bill_number(row)
        title = row[3].strip()
        self.stdout.write(' %s | %s ... ' % (bill_number, title))

        law_number = self._get_law_number(row[17])

        child = DraftLawChild(
            parent=parent,
            bill_number=bill_number,
            title_ka=title,
            law_number=law_number,
        )
        child.save()

        children = DraftLawChild.objects.filter(bill_number=child.bill_number)
        if len(children) > 1:
            if self.force:
                children.exclude(pk=child.pk).delete()
                self.stdout.write('replace existing!')
            else:
                self.stdout.write('keep already existing!')
                child.delete()
                return False
        else:
            self.stdout.write('add new!')

        return True


    def _add_georgian (self, row):
        """Add georgian data to english record.

        This will overwrite previous data.

        @param row: data row
        @type row: [ str ]
        @return: if data could be added
        @rtype: bool
        """
        from draftlaw.models import DraftLaw, DraftLawChild
        bill_number = self._get_bill_number(row)
        self.stdout.write('%s | Adding georgian to english ... ' % bill_number)
        try:
            obj = DraftLaw.objects.get(bill_number=bill_number)
        except DraftLaw.DoesNotExist:
            try:
                obj = DraftLawChild.objects.get(bill_number=bill_number)
            except DraftLawChild.DoesNotExist:
                self.stdout.write('Bill number does not exist yet!')
                return False

        obj.title_ka = row[3].strip()
        if hasattr(obj, 'summary'):
            obj.summary_ka = row[6].strip()
        if hasattr(obj, 'initiator'):
            obj.initiator_ka = row[4].strip()
        if hasattr(obj, 'author'):
            obj.author_ka = row[5].strip()
        obj.save()
        self.stdout.write('OK')

        return True


    def handle (self, *args, **options):
        """Command handler."""
        if options.get('force'):
            self.force = True
        else:
            self.force = False

        if len(args) != 1:
            self.stderr.write('Missing file to read CSV data from!\n')
            return

        rows = csv.reader(open(args[0], 'rb'), delimiter=DELIMITER)
        first = True
        parent = None
        for row in rows:
            if first: # header
                first = False
                continue

            len_row = len(row)
            if len_row not in [COL_KA, COL_EN]:
                self.stdout.write('Invalid draftlaw record, only %d columns.\n' % len_row)
                continue

            if len_row == COL_KA: # this is the georgian version, add to english original
                self._add_georgian(row)
            else:
                if row[2] == '*': # parent
                    parent = self._create_draftlaw(row)
                else: # child
                    self._create_draftlawchild(row, parent)

            self.stdout.write('\n')
