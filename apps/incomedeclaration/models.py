# vim: set fileencoding=utf-8
"""
Model incomedeclaration

Depends on representative.
"""
__docformat__ = 'epytext en'

from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from glt import slughifi


class IncomeDeclaration (models.Model):
    """Defines an income declaration."""
    slug = models.SlugField(max_length=100, editable=False, null=False)
    #: declaration ID
    decl_id = models.CharField(max_length=64, help_text=_('Declaration ID'))
    #: scrape date
    scrape_date = models.DateField(editable=False,
        help_text=_('Date of Scrape Process'))
    #: name of the MP
    name = models.CharField(max_length=255, help_text=_('MP\'s Name'))
    #: declaration date
    date = models.DateField(null=True, help_text=_('Date of Declaration'))
    #: representative to whom this declaration applies (not set on import)
    representative = models.ForeignKey('representative.Representative', related_name='incomedeclaration',
        null=True, help_text=_('Representative, Supplier of this declaration'))


    class Meta:
        ordering = ('decl_id',)


    def save (self, *args, **kwargs):
        max_len = self._meta.get_field('slug').max_length
        self.slug = slughifi(str(self)[:max_len])
        super(IncomeDeclaration, self).save(*args, **kwargs)


    def __unicode__ (self):
        return u'%s %s' % (self.decl_id, self.name)


    @models.permalink
    def get_absolute_url (self, language=None):
        return ('incomedeclaration_detail', [self.slug])



class DeclarationBiography (models.Model):
    """Defines an MP's other included expenses."""
    #: related declaration
    declaration = models.ForeignKey(IncomeDeclaration, related_name='biographies',
        help_text=_('Related Declaration'))
    #: position
    position = models.TextField(help_text=_('Position'))
    #: work contact
    work_contact = models.TextField(help_text=_('Work Contact'))
    #: place, date of birth
    place_dob = models.TextField(help_text=_('Place and Date of Birth'))

    def __unicode__ (self):
        return '%s %s: %s' % (
            self.declaration.decl_id, self.declaration.name, self.position)


    class Meta:
        ordering = ('declaration',)



class DeclarationCash (models.Model):
    """Defines an MP's cash."""
    #: related declaration
    declaration = models.ForeignKey(IncomeDeclaration, related_name='cash',
        help_text=_('Related Declaration'))
    #: name (of the cash holder?)
    name = models.TextField(help_text=_('Name'))
    #: amount
    amt_currency = models.TextField(help_text=_('Amount & Currency'))

    def __unicode__ (self):
        return '%s %s: %s' % (
            self.declaration.decl_id, self.declaration.name, self.amt_currency)


    class Meta:
        ordering = ('declaration',)



class DeclarationContract (models.Model):
    """Defines an MP's contracts."""
    #: related declaration
    declaration = models.ForeignKey(IncomeDeclaration, related_name='contracts',
        help_text=_('Related Declaration'))
    #: name (of the contract owner?)
    name = models.TextField(help_text=_('Name'))
    #: description and value
    desc_value = models.TextField(help_text=_('Description & Value'))
    #: date, period and agency
    date_period_agency = models.TextField(help_text=_('Date Period & Agency'))
    #: financial result
    financial_result = models.TextField(help_text=_('Financial Result'))

    def __unicode__ (self):
        return '%s %s: %s' % (
            self.declaration.decl_id, self.declaration.name, self.desc_value)


    class Meta:
        ordering = ('declaration',)



class DeclarationDeposit (models.Model):
    """Defines an MP's deposits."""
    #: related declaration
    declaration = models.ForeignKey(IncomeDeclaration, related_name='deposits',
        help_text=_('Related Declaration'))
    #: name (of the deposit owner?)
    name = models.TextField(help_text=_('Name'))
    #: name of the bank
    bank = models.TextField(help_text=_('Name of the Bank'))
    #: deposit type
    type = models.TextField(help_text=_('Type of Deposit'))
    #: deposit balance
    balance = models.TextField(help_text=_('Balance'))

    def __unicode__ (self):
        return '%s %s: %s' % (
            self.declaration.decl_id, self.declaration.name, self.balance)


    class Meta:
        ordering = ('declaration',)



class DeclarationEntrepreneurial (models.Model):
    """Defines an MP's entrepreneurial activities."""
    #: related declaration
    declaration = models.ForeignKey(IncomeDeclaration,
        related_name='entrepreneurials', help_text=_('Related Declaration'))
    #: name (of the entrepreneur?)
    name = models.TextField(help_text=_('Name'))
    #: corporation name and address
    corp_name_addr = models.TextField(help_text=_('Corporation Name & Address'))
    #: type of participation
    particn_type = models.TextField(help_text=_('Type of Participation'))
    #: registered with agency
    register_agency = models.TextField(help_text=_('Registered with Agency'))
    #: date of participation
    particn_date = models.TextField(help_text=_('Date of Participation'))
    #: income record
    income_rec = models.TextField(help_text=_('Income Record'))

    def __unicode__ (self):
        return '%s %s: %s' % (
            self.declaration.decl_id, self.declaration.name, self.corp_name_addr)


    class Meta:
        ordering = ('declaration',)



class DeclarationFamily (models.Model):
    """Defines an MP's family."""
    #: related declaration
    declaration = models.ForeignKey(IncomeDeclaration, related_name='family',
        help_text=_('Related Declaration'))
    #: first name
    name = models.TextField(help_text=_('First Name'))
    #: last name
    surname = models.TextField(help_text=_('Last Name'))
    #: place of birth
    pob = models.TextField(help_text=_('Place of Birth'))
    #: date of birth
    dob = models.TextField(help_text=_('Date of Birth'))
    #: relation to the MP
    relation = models.TextField(help_text=_('Relation to MP'))


    def __unicode__ (self):
        return '%s %s: %s %s' % (
            self.declaration.decl_id, self.declaration.name,
            self.name, self.surname)


    class Meta:
        ordering = ('declaration',)



class DeclarationGift (models.Model):
    """Defines an MP's gifts."""
    #: related declaration
    declaration = models.ForeignKey(IncomeDeclaration, related_name='gifts',
        help_text=_('Related Declaration'))
    #: name (of the giver?)
    name = models.TextField(help_text=_('Name'))
    #: description and value
    desc_value = models.TextField(help_text=_('Description & Value'))
    #: relation to giver
    giver_rel = models.TextField(help_text=_('Relation to Giver'))

    def __unicode__ (self):
        return '%s %s: %s' % (
            self.declaration.decl_id, self.declaration.name, self.desc_value)


    class Meta:
        ordering = ('declaration',)



class DeclarationOtherInclExpense (models.Model):
    """Defines an MP's other included expenses."""
    #: related declaration
    declaration = models.ForeignKey(IncomeDeclaration,
        related_name='otherinclexpenses', help_text=_('Related Declaration'))
    #: recipient issuer
    recip_issuer = models.TextField(help_text=_('Recipient Issuer'))
    #: type
    type = models.TextField(help_text=_('Type'))
    #: amount
    amount = models.TextField(help_text=_('Amount'))

    def __unicode__ (self):
        return '%s %s: %s' % (
            self.declaration.decl_id, self.declaration.name, self.recip_issuer)


    class Meta:
        ordering = ('declaration',)



class DeclarationProperty (models.Model):
    """Defines an MP's properties."""
    #: related declaration
    declaration = models.ForeignKey(IncomeDeclaration,
        related_name='properties', help_text=_('Related Declaration'))
    #: name shares
    name_shares = models.TextField(help_text=_('Name & Shares'))
    #: property type
    prop_type = models.TextField(help_text=_('Property Type'))
    #: description
    description = models.TextField(help_text=_('Description'))
    #: other owners
    co_owners = models.TextField(help_text=_('Co Owners'))

    def __unicode__ (self):
        return '%s %s: %s' % (
            self.declaration.decl_id, self.declaration.name, self.description)


    class Meta:
        ordering = ('declaration',)



class DeclarationRealEstate (models.Model):
    """Defines an MP's real estates."""
    #: related declaration
    declaration = models.ForeignKey(IncomeDeclaration,
        related_name='realestates', help_text=_('Related Declaration'))
    #: name shares
    name_shares = models.TextField(help_text=_('Name & Shares'))
    #: property type
    prop_type = models.TextField(help_text=_('Property Type'))
    #: location / area
    loc_area = models.TextField(help_text=_('Location & Area'))
    #: other owners
    co_owners = models.TextField(help_text=_('Co Owners'))

    def __unicode__ (self):
        return '%s %s: %s' % (
            self.declaration.decl_id, self.declaration.name, self.prop_type)


    class Meta:
        ordering = ('declaration',)



class DeclarationSecurity (models.Model):
    """Defines an MP's securities."""
    #: related declaration
    declaration = models.ForeignKey(IncomeDeclaration,
        related_name='securities', help_text=_('Related Declaration'))
    #: name (of the security holder?)
    name = models.TextField(help_text=_('Name'))
    #: issuer
    issuer = models.TextField(help_text=_('Issuer'))
    #: type
    type = models.TextField(help_text=_('Type'))
    #: price
    price = models.TextField(help_text=_('Price'))
    #: quantitiy
    quantity = models.TextField(help_text=_('Quantity'))

    def __unicode__ (self):
        return '%s %s: %s' % (
            self.declaration.decl_id, self.declaration.name, self.issuer)


    class Meta:
        ordering = ('declaration',)




class DeclarationWage (models.Model):
    """Defines an MP's wages."""
    #: related declaration
    declaration = models.ForeignKey(IncomeDeclaration, related_name='wages',
        help_text=_('Related Declaration'))
    #: name (of the employee?)
    name = models.TextField(help_text=_('Name'))
    #: description of workplace
    desc_workplace = models.TextField(help_text=_('Description of Workplace'))
    #: description of job
    desc_job = models.TextField(help_text=_('Description of Job'))
    #: income record
    income_rec = models.TextField(help_text=_('Income Record'))

    def __unicode__ (self):
        return '%s %s: %s' % (
            self.declaration.decl_id, self.declaration.name, self.desc_job)


    class Meta:
        ordering = ('declaration',)



# There must be a bug in CMS plugin models. Without exception handler, on
# running an admin command, the class definition would yield:
#  File "/votingrecord/models.py", line 70, in <module>
#      class VotingRecordPluginConf (CMSPlugin):
#        File "/usr/local/lib/python2.7/dist-packages/cms/models/pluginmodel.py", line 56, in __new__
#            table_name = 'cmsplugin_%s' % splitted[1]
#            IndexError: list index out of range
try:
    class IncomeDeclarationPluginConf (CMSPlugin):
        """Configuration for income declaration plugin."""
        #: title of the plugin
        title = models.CharField(max_length=32, default=_('Income Declarations'))
except IndexError:
    pass
