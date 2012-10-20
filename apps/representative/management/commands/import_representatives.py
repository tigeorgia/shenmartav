# vim: set fileencoding=utf-8
# -*- coding: utf-8 -*
"""
Command import_people as provided by CIPPD

Depends on popit.
"""
__docformat__ = 'epytext en'

import csv
#from datetime import datetime
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from django.db import transaction
from optparse import make_option

import glt
from popit.models import *
from representative.models import Representative, AdditionalInformation, Url, Unit, Party


#: CSV delimiter
DELIMITER = '|'


class Command (BaseCommand):
    """Command to import people from a CSV file."""
    #: allowed arguments to the command
    args = '<filename>'
    #: help string
    help = 'Imports people records from a CSV file.'
    #: custom options
    option_list = BaseCommand.option_list + (
        make_option(
            '--force',
            action='store_true',
            dest='force',
            default=False,
            help='Force replacing people.'
        ),
    )
    #: force overwriting representative even though scrape date is not newer
    force = False
    #: unit where all imported people are a member of
    unit = None


    def _get_isodate(self, date):
        """Convert given date to a database-compatible ISO date.

        The dates in the CSV file are still in a horrible mess.

        @param date: date to convert
        @type date: str
        @return: date in ISO format
        @rtype: str
        """
        fmt = 'Wrong date format: %s\n'
        parts = date.strip().split('.')
        parts = [x.strip() for x in parts]
        parts_len = len(parts)

        if parts_len == 1: # only got year
            parts.insert(0, '01')
            parts.insert(0, '01')
        elif parts_len == 2: # only got year + month
            parts.insert(0, '01')

        if len(parts[0]) < 2:
            if not parts[0] or parts[0] == '0':
                parts[0] = '01'
            else:
                parts[0] = '0' + parts[0]

        if len(parts[1]) < 2:
            if not parts[1] or parts[1] == '0':
                parts[1] = '01'
            else:
                parts[1] = '0' + parts[1]

        if len(parts[2]) != 4:
            self.stderr.write(fmt % date)
            return None

        try:
            return '%s-%s-%s' % (parts[2], parts[1], parts[0])
        except IndexError:
            self.stderr.write(fmt % date)
            return None


    def _get_data (self, row, index):
        """Get one date item ouf of the row.

        @param row: data row
        @type row: [ str ]
        @param index: index of data item in row
        @type index: int
        """
        return row[index].strip().decode('utf-8')


    def _add_representative_data (self, row, representative):
        """Add data to a representative record.

        @param row: data row
        @type row: [ str ]
        @param representative: a representative
        @type representative: representative.Representative
        """
        representative.is_majoritarian = (self._get_data(row, 2) == u'მაჟორიტარი')
        representative.electoral_district = self._get_data(row, 4)
        representative.elected = self._get_data(row, 5)
        representative.pob = self._get_data(row, 8)
        representative.family_status = self._get_data(row, 9)
        representative.education = ';'.join([
            self._get_data(row, 10), self._get_data(row, 11),
            self._get_data(row, 12), self._get_data(row, 13)])
        representative.contact_address_phone = self._get_data(row, 14)

        data = self._get_data(row, 15)
        if data:
            url = Url(representative=representative, label=url, url=url)
            url.save()

        for i in xrange(38, 50):
            data = self._get_data(row, i)
            if data:
                info = AdditionalInformation(
                    representative=representative, value=data)
                info.save()

        representative.save()


    @transaction.commit_on_success
    def _create_representative (self, row):
        """Create a complete Representative record.

        @param row: data row
        @type row: [ str ]
        @return: a representative
        @rtype: representative.Representative
        """
        name = glt.firstname_first(row[1])
        self.stdout.write('%s | Representative: %s ... ' % (row[0], name))

        dob = self._get_isodate(row[7].decode('utf-8'))
        representative = Representative(
            date_of_birth=dob,
            description=row[6].decode('utf-8').strip(),
            unit=self.unit)
        representative.save()

        pname = PersonName(person=representative, name=name, main=True)
        pname.save()

        people = Representative.objects.filter(slug=representative.slug)
        if len(people) > 1:
            if self.force:
                people.exclude(pk=representative.pk).delete()
                self.stdout.write('replace existing!\n')
                self._add_representative_data(row, representative)
                return representative
            else:
                self.stdout.write('keep already existing!\n')
                slug = representative.slug
                representative.delete()
                return Representative.objects.get(slug=slug)
        else:
            self.stdout.write('add new!\n')
            self._add_representative_data(row, representative)
            return representative


    @transaction.commit_on_success
    def _create_party (self, representative, row):
        """Create a party.

        @param representative: a representative
        @type representative: representative.Representative
        @param row: data row
        @type row: [ str ]
        @return: an organisation
        @rtype: popit.Organisation
        """
        name = row[3].decode('utf-8').strip()
        self.stdout.write(' Party %s ... ' % (name))

        party = Party()
        party.save()
        OrganisationName(organisation=party, name=name, main=True).save()

        parties = Party.objects.filter(slug=party.slug)
        if len(parties) > 1:
            self.stdout.write('keep already existing!\n')
            slug = party.slug
            party.delete()
            party = Party.objects.get(slug=slug)
        else:
            self.stdout.write('add new!\n')
        party.unit.add(self.unit)

        representative.party = party
        representative.save()

        return party


    def _get_startend_dates (self, dates):
        """Get work experience start and end dates.

        @param dates: start and end dates
        @type dates: str
        @return: start and end dates
        @rtype: ( str, str )
        """
        dates_len = len(dates)
        if dates_len == 2:
            start_date = self._get_isodate(dates[0])
            end_date = self._get_isodate(dates[1])
        elif dates_len == 1:
            start_date = self._get_isodate(dates[0])
            end_date = None
        else:
            start_date = None
            end_date = None

        return start_date, end_date


    @transaction.commit_on_success
    def _create_positions (self, representative, row):
        """Create Position records for the given representative.

        @param representative: a representative
        @type representative: representative.Representative
        @param row: data row
        @type row: [ str ]
        @return: all positions
        @rtype: [ representative.Representative ]
        """
        positions = []
        max_length = Position._meta.get_field('title').max_length
        sep = '-'

        for i in xrange(16, 38): # work experiences
            if not row[i]: continue

            experience = row[i].strip().replace('–', sep).split(sep)
            if len(experience) < 3:
                msg = 'Faulty Work Experience, lumping everything together:\n'
                self.stderr.write(msg)
                title = sep.join(experience)
            else:
                title = sep.join(experience[2:])
            title = title.strip().decode('utf-8')[:max_length-1]
            self.stdout.write(' Position %s ... ' % (title))

            existing = Position.objects.filter(
                person=representative, title=title)
            if len(existing) > 0:
                if self.force:
                    self.stdout.write('replace existing!\n')
                    existing.delete()
                else:
                    self.stdout.write('keep already existing!\n')
                    continue
            else:
                self.stdout.write('add new!\n')

            start_date, end_date = self._get_startend_dates(experience[0:2])
            try:
                position = Position(person=representative, title=title,
                    start_date=start_date, end_date=end_date)
            except (ValidationError, NameError):
                self.stderr.write('Yet another date formatting error!\n')
            else:
                position.save()
                positions.append(position)

        return positions



    def handle (self, *args, **options):
        """Command handler."""
        if options.get('force'):
            self.force = True
        else:
            self.force = False

        if len(args) < 1:
            self.stderr.write('Missing file to read CSV data from!\n')
            return

        if len(args) < 2:
            self.stdout.write('Assuming unit "parliament"\n')
            self.unit = Unit.objects.get(short='parliament')
        else:
            self.unit = Unit.objects.get(short=args[1])
            self.stdout.write('Using unit "%s"\n' % self.unit)

        rows = csv.reader(open(args[0], 'rb'), delimiter=DELIMITER)
        for row in rows:
            if not row or not row[0]: continue # headers

            if len(row) < 50:
                self.stdout.write('Invalid representative record.\n')
                continue

            representative = self._create_representative(row)
            if not representative: continue
            party = self._create_party(representative, row)
            positions = self._create_positions(representative, row)
            self.stdout.write('\n')
