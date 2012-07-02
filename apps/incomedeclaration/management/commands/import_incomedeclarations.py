# vim: set fileencoding=utf-8
"""
Command import_incomedeclaration
"""
__docformat__ = 'epytext en'

import os, csv, datetime
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from optparse import make_option

from ...models import IncomeDeclaration, DeclarationSecurity,\
    DeclarationFamily, DeclarationContract, DeclarationDeposit,\
    DeclarationCash, DeclarationGift, DeclarationEntrepreneurial,\
    DeclarationRealEstate, DeclarationWage, DeclarationProperty,\
    DeclarationProperty, DeclarationOtherInclExpense, DeclarationBiography


class Command (BaseCommand):
    """Command to import income declarations from CSV files."""
    #: allowed arguments to the command
    args = '<dirname>'
    #: help string
    help = 'Imports a income declarations from a directory with CSV files.'
    #: list of declaration IDs for whose adding is always ok.
    addok = []
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


    def __init__ (self, *args, **kwargs):
        """Constructor."""
        super(Command, self).__init__()

        #: mapping of CSV file names to functions
        self.sectionmap = {
            'biography': self._get_biography,
            'cash': self._get_cash,
            'contracts': self._get_contract,
            'deposits': self._get_deposit,
            'entrepreneurial': self._get_entrepreneurial,
            'family': self._get_family,
            'gifts': self._get_gift,
            'other_incl_expenses': self._get_otherinclexpense,
            'property': self._get_property,
            'real_estate': self._get_realestate,
            'securities': self._get_security,
            'wages': self._get_wage
        }



    def _get_filename (self, dirname, section):
        """
        Get filename for given section.

        @param dirname: directory name with files
        @type dirname: str
        @param section: section to construct filename for
        @type section: str
        @return: filename for given section
        @type: str
        """
        return dirname + os.sep + section + '.csv'


    def _create_declaration (self, row):
        """
        Create an income declaration from given row.

        @param row: data required to create an income declaration
        @type row: [ str ]
        @return: income declaration
        @rtype: IncomeDeclaration
        """
        self.stdout.write("%s: Creating income declaration.\n" % row[0])
        if not row[3]:
            date = None
        else:
            date = datetime.datetime.strptime(row[3], '%d/%m/%Y')

        declaration = IncomeDeclaration(
            decl_id=row[0], scrape_date=row[1], name=row[2], date=date)
        declaration.save()
        return declaration


    def _get_declaration (self, row):
        """
        Get an income declaration object for given row.

        @param row: data required to create an income declaration
        @type row: [ str ]
        @return: income declaration
        @rtype: IncomeDeclaration or None
        """
        existing = IncomeDeclaration.objects.filter(decl_id=row[0])

        if len(existing) == 0:
            declaration = self._create_declaration(row)
            self.addok.append(declaration.decl_id)
            return declaration

        else:
            declaration = existing[0]
            if declaration.decl_id in self.addok:
                return declaration

            scrape_date = datetime.datetime.strptime(row[1], '%Y-%m-%d')
            if self.force or scrape_date.date() > declaration.scrape_date:
                self.stdout.write("%s: Deleting old declaration.\n" % row[0])
                declaration.delete() # this deletes all relationships as well!
                declaration = self._create_declaration(row)
                # after recreation adding is always ok
                self.addok.append(declaration.decl_id)
                return declaration
            else:
                fmt = "%s: Scrape date %s already imported.\n"
                self.stdout.write(fmt % (row[0], row[1]))
                return None


    def _get_biography (self, declaration, row):
        """
        Get declaration biography.

        @param declaration: related declaration
        @type declaration: IncomeDeclaration
        @param row: data required to create a declaration biography object
        @type row: [ str ]
        @return: declaration biography object
        @rtype: DeclarationBiography
        """
        return DeclarationBiography(declaration=declaration,
            position=row[4], work_contact=row[5], place_dob=row[6])


    def _get_cash (self, declaration, row):
        """
        Get declaration cash.

        @param declaration: related declaration
        @type declaration: IncomeDeclaration
        @param row: data required to create a declaration cash object
        @type row: [ str ]
        @return: declaration cash object
        @rtype: DeclarationCash
        """
        return DeclarationCash(declaration=declaration,
            name=row[4], amt_currency=row[5])


    def _get_contract (self, declaration, row):
        """
        Get declaration contract.

        @param declaration: related declaration
        @type declaration: IncomeDeclaration
        @param row: data required to create a declaration contract object
        @type row: [ str ]
        @return: declaration contract object
        @rtype: DeclarationContract
        """
        return DeclarationContract(declaration=declaration,
            name=row[4], desc_value=row[5], date_period_agency=row[6],
            financial_result=row[7])


    def _get_deposit (self, declaration, row):
        """
        Get declaration deposit.

        @param declaration: related declaration
        @type declaration: IncomeDeclaration
        @param row: data required to create a declaration deposit object
        @type row: [ str ]
        @return: declaration deposit object
        @rtype: DeclarationDeposit
        """
        return DeclarationDeposit(declaration=declaration,
            name=row[4], bank=row[5], type=row[6], balance=row[7])


    def _get_entrepreneurial (self, declaration, row):
        """
        Get declaration entrepreneurial.

        @param declaration: related declaration
        @type declaration: IncomeDeclaration
        @param row: data required to create a declaration entrepreneurial object
        @type row: [ str ]
        @return: declaration entrepreneurial object
        @rtype: DeclarationEntrepreneurial
        """
        return DeclarationEntrepreneurial(declaration=declaration,
            name=row[4], corp_name_addr=row[5], particn_type=row[6],
            register_agency=row[7], particn_date=row[8],
            income_rec=row[9])


    def _get_family (self, declaration, row):
        """
        Get declaration family.

        @param declaration: related declaration
        @type declaration: IncomeDeclaration
        @param row: data required to create a declaration family object
        @type row: [ str ]
        @return: declaration family object
        @rtype: DeclarationContract
        """
        return DeclarationFamily(declaration=declaration,
            name=row[4], surname=row[5], pob=row[6], dob=row[7],
            relation=row[8])


    def _get_gift (self, declaration, row):
        """
        Get declaration gift.

        @param declaration: related declaration
        @type declaration: IncomeDeclaration
        @param row: data required to create a declaration gift object
        @type row: [ str ]
        @return: declaration gift object
        @rtype: DeclarationGift
        """
        return DeclarationGift(declaration=declaration,
            name=row[4], desc_value=row[5], giver_rel=row[6])


    def _get_otherinclexpense (self, declaration, row):
        """
        Get declaration other included expense.

        @param declaration: related declaration
        @type declaration: IncomeDeclaration
        @param row: data required to create a declaration other included expense object
        @type row: [ str ]
        @return: declaration other included expense object
        @rtype: DeclarationOtherInclExpense
        """
        return DeclarationOtherInclExpense(declaration=declaration,
            recip_issuer=row[4], type=row[5], amount=row[6])


    def _get_property (self, declaration, row):
        """
        Get declaration property.

        @param declaration: related declaration
        @type declaration: IncomeDeclaration
        @param row: data required to create a declaration property object
        @type row: [ str ]
        @return: declaration property object
        @rtype: DeclarationProperty
        """
        return DeclarationProperty(declaration=declaration,
            name_shares=row[4], prop_type=row[5], description=row[6],
            co_owners=row[7])


    def _get_realestate (self, declaration, row):
        """
        Get declaration real estate.

        @param declaration: related declaration
        @type declaration: IncomeDeclaration
        @param row: data required to create a declaration real estate object
        @type row: [ str ]
        @return: declaration real estate object
        @rtype: DeclarationRealEstate
        """
        return DeclarationRealEstate(declaration=declaration,
            name_shares=row[4], prop_type=row[5], loc_area=row[6],
            co_owners=row[7])


    def _get_security (self, declaration, row):
        """
        Get declaration security.

        @param declaration: related declaration
        @type declaration: IncomeDeclaration
        @param row: data required to create a declaration security object
        @type row: [ str ]
        @return: declaration security object
        @rtype: DeclarationSecurity
        """
        return DeclarationSecurity(declaration=declaration,
            name=row[4], issuer=row[5], type=row[6], price=row[7],
            quantity=row[8])


    def _get_wage (self, declaration, row):
        """
        Get declaration wage.

        @param declaration: related declaration
        @type declaration: IncomeDeclaration
        @param row: data required to create a declaration bgiography object
        @type row: [ str ]
        @return: declaration wage object
        @rtype: DeclarationWage
        """
        return DeclarationWage(declaration=declaration,
            name=row[4], desc_workplace=row[5], desc_job=row[6],
            income_rec=row[7])


    @transaction.commit_on_success
    def _handle_section (self, dirname, section):
        """
        Handle one income declaration section.

        @param dirname: directory name with files
        @type dirname: str
        @param section: section to construct filename for
        @type section: str
        """
        self.stdout.write("Handling %s.\n" % section)
        filename = self._get_filename(dirname, section)
        rows = csv.reader(open(filename, 'r'), delimiter='|')
        declaration = None

        for row in rows:
            if not declaration or row[0] != declaration.decl_id:
                declaration = self._get_declaration(row)
            if not declaration:
                continue

            self.stdout.write("%s: Adding %s%s.\n" % (row[0], section, self.force))
            obj = self.sectionmap[section](declaration, row)
            obj.save()


    def handle (self, *args, **options):
        """Command handler."""
        if len(args) != 1:
            self.stderr.write("Missing directory to read CSV files from!\n")
            return

        if options.get('force'):
            self.force = ' (forced)'
        else:
            self.force = '' # also evaluates as False


        for section in self.sectionmap.iterkeys():
            self._handle_section(args[0], section)
