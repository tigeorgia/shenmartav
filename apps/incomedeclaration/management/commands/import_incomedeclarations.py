# -*- coding: utf-8 -*-

"""
Command import_incomedeclaration
"""
__docformat__ = 'epytext en'

import os, csv, datetime
import codecs
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from optparse import make_option

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
        from ...models import IncomeDeclaration

        self.stdout.write("%s: Creating income declaration.\n" % row[0])

        name = row[2].strip().decode('utf-8')

        if not row[3]:
            date = None
        else:
            date = datetime.datetime.strptime(row[3].strip(), '%d/%m/%Y')

        declaration = IncomeDeclaration(
            decl_id=row[0].strip().decode('utf-8-sig'),
            scrape_date=row[1].strip(),
            name_en=name, name_ka=name,
            date=date
        )
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
        from ...models import IncomeDeclaration
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
        position = row[5].strip()
        work_contact = row[6].strip()
        place_dob = row[7].strip()
        from ...models import DeclarationBiography
        return DeclarationBiography(declaration=declaration,
            position_en=position, position_ka=position,
            work_contact_en=work_contact, work_contact_ka=work_contact,
            place_dob_en=place_dob, place_dob_ka=place_dob
        )


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
        name = row[5].strip()
        amt_currency = row[6].strip()
        from ...models import DeclarationCash
        return DeclarationCash(declaration=declaration,
            name_en=name, name_ka=name,
            amt_currency_en=amt_currency, amt_currency_ka=amt_currency
        )


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
        name = row[5].strip()
        desc_value = row[6].strip()
        date_period_agency = row[7].strip()
        financial_result = row[8].strip()
        from ...models import DeclarationContract
        return DeclarationContract(declaration=declaration,
            name_en=name, name_ka=name,
            desc_value_en=desc_value, desc_value_ka=desc_value,
            date_period_agency_en=date_period_agency, date_period_agency_ka=date_period_agency,
            financial_result_en=financial_result, financial_result_ka=financial_result
        )


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
        name = row[5].strip()
        bank = row[6].strip()
        deposit_type = row[7].strip()
        balance = row[8].strip()
        from ...models import DeclarationDeposit 
        return DeclarationDeposit(declaration=declaration,
            name_en=name, name_ka=name,
            bank_en=bank, bank_ka=bank,
            type_en=deposit_type, type_ka=deposit_type,
            balance_en=balance, balance_ka=balance
        )


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
        name = row[5].strip()
        corp_name_addr = row[6].strip()
        particn_type = row[7].strip()
        register_agency = row[8].strip()
        particn_date = row[9].strip()
        income_rec = row[10].strip()
        from ...models import DeclarationEntrepreneurial
        return DeclarationEntrepreneurial(declaration=declaration,
            name_en=name, name_ka=name,
            corp_name_addr_en=corp_name_addr, corp_name_addr_ka=corp_name_addr,
            particn_type_en=particn_type, particn_type_ka=particn_type,
            register_agency_en=register_agency, register_agency_ka=register_agency,
            particn_date_en=particn_date, particn_date_ka=particn_date,
            income_rec_en=income_rec, income_rec_ka=income_rec
        )


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
        name = row[5].strip()
        surname = row[6].strip()
        pob = row[7].strip()
        dob = row[8].strip()
        relation = row[9].strip()
        from ...models import DeclarationFamily
        return DeclarationFamily(declaration=declaration,
            name_en=name, name_ka=name,
            surname_en=surname, surname_ka=surname,
            pob_en=pob, pob_ka=pob,
            dob_en=dob, dob_ka=dob,
            relation_en=relation, relation_ka=relation
        )


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
        name = row[5].strip()
        desc_value = row[6].strip()
        giver_rel = row[7].strip()
        from ...models import DeclarationGift
        return DeclarationGift(declaration=declaration,
            name_en=name, name_ka=name,
            desc_value_en=desc_value, desc_value_ka=desc_value,
            giver_rel_en=giver_rel, giver_rel_ka=giver_rel
        )


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
        recip_issuer = row[5].strip()
        other_type = row[6].strip()
        amount = row[7].strip()
        from ...models import DeclarationOtherInclExpense
        return DeclarationOtherInclExpense(declaration=declaration,
            recip_issuer_en=recip_issuer, recip_issuer_ka=recip_issuer,
            type_en=other_type, type_ka=other_type,
            amount_en=amount, amount_ka=amount
        )


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
        name_shares = row[5].strip()
        prop_type = row[6].strip()
        description = row[7].strip()
        co_owners = row[8].strip()
        from ...models import DeclarationProperty
        return DeclarationProperty(declaration=declaration,
            name_shares_en=name_shares, name_shares_ka=name_shares,
            prop_type_en=prop_type, prop_type_ka=prop_type,
            description_en=description, description_ka=description,
            co_owners_en=co_owners, co_owners_ka=co_owners
        )


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
        name_shares = row[5].strip()
        prop_type = row[6].strip()
        loc_area = row[7].strip()
        co_owners = row[8].strip()
        from ...models import DeclarationRealEstate
        return DeclarationRealEstate(declaration=declaration,
            name_shares_en=name_shares, name_shares_ka=name_shares,
            prop_type_en=prop_type, prop_type_ka=prop_type,
            loc_area_en=loc_area, loc_area_ka=loc_area,
            co_owners_en=co_owners, co_owners_ka=co_owners
        )


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
        name = row[5].strip()
        issuer = row[6].strip()
        security_type = row[7].strip()
        price = row[8].strip()
        quantity = row[9].strip()
        from ...models import DeclarationSecurity
        return DeclarationSecurity(declaration=declaration,
            name_en=name, name_ka=name,
            issuer_en=issuer, issuer_ka=issuer,
            type_en=security_type, type_ka=security_type,
            price_en=price, price_ka=price,
            quantity_en=quantity, quantity_ka=quantity
        )


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
        name = row[5].strip()
        desc_workplace = row[6].strip()
        desc_job = row[7].strip()
        income_rec = row[8].strip()
        from ...models import DeclarationWage
        return DeclarationWage(declaration=declaration,
            name_en=name, name_ka=name,
            desc_workplace_en=desc_workplace, desc_workplace_ka=desc_workplace,
            desc_job_en=desc_job, desc_job_ka=desc_job,
            income_rec_en=income_rec, income_rec_ka=income_rec
        )


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
