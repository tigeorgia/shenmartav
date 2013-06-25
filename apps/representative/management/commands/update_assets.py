# vim: set fileencoding=utf-8
# -*- coding: utf-8 -*
"""
Command update_assets to update parliamentarians' assets as defined in income
declarations. It updates the fields for salary, expenses, property & assets.

Depends on representative and incomedeclaration
"""
__docformat__ = 'epytext en'

from django.core.management.base import BaseCommand
from django.db import transaction


class Command (BaseCommand):
    """Command to update parliamentarians' assets."""
    #: help string
    help = 'Updates parliamentarians\' assets.'


    def _find_declaration (self, name):
        """Finds the latest income declaration for given name.

        @param name: name of the declaration's submitter
        @type name: str
        @return: name's latest income declaration
        @rtype: incomedeclaration.IncomeDeclaration
        """
        from representative.models import NAME_MINLEN
        from incomedeclaration.models import IncomeDeclaration
        first, last = name.split(u' ', 1)
        decls = IncomeDeclaration.objects.filter(name__icontains=last)
        if not decls:
            return None

        if len(decls) == 1:
            return decls[0]

        decls = decls.filter(name__icontains=first).order_by('-date')
        if decls:
            return decls[0]

        # people might have slightly different first names in declaration /
        # person sets, so we only look for the first CHARS_FIRSTNAME
        first = first[0:NAME_MINLEN]
        decls = decls.filter(name__icontains=first).order_by('-date')
        if decls:
            return decls[0]

        return None


    def _get_salary (self, decl, name):
        """Get salary (wages) from given declaration.

        @param decl: declaration
        @type decl: incomedeclaration.IncomeDeclaration
        @param name: name of the representative
        @type name: popit.PersonName
        @return: salary from income declaration
        @rtype: int
        """
        wages = []
        for w in decl.wages.all():
            # wages might include other people, e.g. family
            if not (w.name == name.name_en or w.name == name.name_ka):
                continue

            income = w.income_rec.split()
            try:
                if income[1] != 'GEL':
                    fmt = u'Ignoring Non-GEL value for income in wages: %s.\n'
                    self.stderr.write(fmt % w.income_rec)
                else:
                    wages.append(float(income[0]))
            except IndexError:
                pass

        return int(sum(wages));


    def _get_other_income (self, decl):
        """Get other income (entrepreneurials) from given declaration.

        @param decl: declaration
        @type decl: incomedeclaration.IncomeDeclaration
        @return: other income from income declaration
        @rtype: int
        """
        other = []
        for e in decl.entrepreneurials.all():
            income = e.income_rec.split()
            try:
                if income[1] != 'GEL':
                    fmt = u'Ignoring Non-GEL value for income in entrepreneurials: %s.\n'
                    self.stderr.write(fmt % e.income_rec)
                else:
                    other.append(float(income[0]))
            except IndexError:
                pass
        return int(sum(other))


    def _get_expenses (self, decl):
        """Get expenses value from given declaration.

        @param decl: declaration
        @type decl: incomedeclaration.IncomeDeclaration
        @return: expenses from income declaration
        @rtype: str
        """
        expenses = [e.amount for e in decl.otherinclexpenses.all()]
        return '; '.join(expenses)


    def _get_property (self, decl):
        """Get property & assets value from given declaration.

        @param decl: declaration
        @type decl: incomedeclaration.IncomeDeclaration
        @return: property & assets from income declaration
        @rtype: str
        """
        properties = [p.description for p in decl.properties.all()]
        properties += [r.prop_type for r in decl.realestates.all()]
        return '; '.join(properties)


    @transaction.commit_on_success
    def _update (self, representative, decl):
        """Update person's assets with given declaration.

        @param representative: a representative
        @type representative: representative.Representative
        @param decl: representative\'s income declaration
        @type decl: incomedeclaration.IncomeDeclaration
        @return: output message
        @rtype: [str]
        """
        msg = []
        name = representative.names.all()[0]
        representative.salary = self._get_salary(decl, name)
        if representative.salary:
            msg.append(u'i: %d' % representative.salary)

        representative.other_income = self._get_other_income(decl)
        if representative.other_income:
            msg.append(u' o: %d' % representative.other_income)

        representative.expenses = self._get_expenses(decl)
        if representative.expenses:
            msg.append(u' e: %s' % representative.expenses)

        representative.property_assets = self._get_property(decl)
        if representative.property_assets:
            msg.append(' p: %s' % representative.property_assets)

        representative.save()
        return msg


    @transaction.commit_on_success
    def handle (self, *args, **options):
        """Command handler."""
        from representative.models import Representative
        decl_ids = {}
        for representative in Representative.objects.all():
            self.stdout.write(u'%s: ' % representative.name)

            name = representative.names.all()[0]
            # look for georgian name first
            decl = self._find_declaration(name.name_ka)
            if not decl: # then check english
                decl = self._find_declaration(representative.name.name_en)
            if not decl:
                self.stdout.write('\n')
                continue

            if decl.decl_id in decl_ids.keys():
                fmt = u'Ignoring same declaration for different people %s <> %s.\n'
                self.stderr.write(fmt % (decl_ids[decl.decl_id], representative.name))
                continue
            else:
                decl_ids[decl.decl_id] = representative.name
                self.stdout.write(u'%s ' % decl.decl_id)

            decl.representative = representative
            decl.save()
            msg = self._update(representative, decl)
            # tired of Python's unicode awkwardness, worse in 2.6 than 2.7
            print ''.join(msg)
            #self.stdout.write(''.join(msg) + '\n')
