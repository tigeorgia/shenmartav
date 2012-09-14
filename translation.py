from modeltranslation.translator import translator, TranslationOptions



from question.models import Question

class QuestionTranslationOptions (TranslationOptions):
    fields = ('first_name', 'last_name', 'question', 'answer',)
translator.register(Question, QuestionTranslationOptions)



from representative.models import Representative, AdditionalInformation, Unit, Term

class RepresentativeTranslationOptions (TranslationOptions):
    fields = ('committee', 'faction', 'electoral_district', 'elected',
        'pob', 'family_status', 'education', 'contact_address_phone',
        'expenses', 'property_assets',)
translator.register(Representative, RepresentativeTranslationOptions)

class AdditionalInformationTranslationOptions (TranslationOptions):
    fields = ('value',)
translator.register(AdditionalInformation, AdditionalInformationTranslationOptions)

class UnitTranslationOptions (TranslationOptions):
    fields = ('name',)
translator.register(Unit, UnitTranslationOptions)

class TermTranslationOptions (TranslationOptions):
    fields = ('name',)
translator.register(Term, TermTranslationOptions)


from popit.models import Person, PersonName, Organisation, OrganisationName, Position

class PersonTranslationOptions (TranslationOptions):
    fields = ('description',)
translator.register(Person, PersonTranslationOptions)

class PersonNameTranslationOptions (TranslationOptions):
    fields = ('title', 'name',)
translator.register(PersonName, PersonNameTranslationOptions)

class OrganisationTranslationOptions (TranslationOptions):
    fields = ('summary', )
translator.register(Organisation, OrganisationTranslationOptions)

class OrganisationNameTranslationOptions (TranslationOptions):
    fields = ('name',)
translator.register(OrganisationName, OrganisationNameTranslationOptions)

class PositionTranslationOptions (TranslationOptions):
    fields = ('title', 'place', 'note',)
translator.register(Position, PositionTranslationOptions)



from draftlaw.models import DraftLaw, DraftLawDiscussion, DraftLawChild

class DraftLawTranslationOptions (TranslationOptions):
    fields = ('title', 'initiator', 'author', 'status', 'summary', 'full_text',)
translator.register(DraftLaw, DraftLawTranslationOptions)

class DraftLawDiscussionTranslationOptions (TranslationOptions):
    fields = ('place',)
translator.register(DraftLawDiscussion, DraftLawDiscussionTranslationOptions)

class DraftLawChildTranslationOptions (TranslationOptions):
    fields = ('title',)
translator.register(DraftLawChild, DraftLawChildTranslationOptions)



from smsalert.models import SMSAlert
class SMSAlertTranslationOptions (TranslationOptions):
    fields = ('text',)
translator.register(SMSAlert, SMSAlertTranslationOptions)



from votingrecord.models import VotingRecord

class VotingRecordTranslationOptions (TranslationOptions):
    fields = ('name',)
translator.register(VotingRecord, VotingRecordTranslationOptions)



from incomedeclaration.models import IncomeDeclaration, DeclarationSecurity,\
    DeclarationFamily, DeclarationContract, DeclarationDeposit,\
    DeclarationCash, DeclarationGift, DeclarationEntrepreneurial,\
    DeclarationRealEstate, DeclarationWage, DeclarationProperty,\
    DeclarationOtherInclExpense, DeclarationBiography

class IncomeDeclarationTranslationOptions (TranslationOptions):
    fields = ('name',)
translator.register(IncomeDeclaration, IncomeDeclarationTranslationOptions)

class DeclarationBiographyTranslationOptions (TranslationOptions):
    fields = ('position', 'work_contact', 'place_dob',)
translator.register(DeclarationBiography, DeclarationBiographyTranslationOptions)

class DeclarationCashTranslationOptions (TranslationOptions):
    fields = ('name', 'amt_currency',)
translator.register(DeclarationCash, DeclarationCashTranslationOptions)

class DeclarationContractTranslationOptions (TranslationOptions):
    fields = ('name', 'desc_value', 'date_period_agency', 'financial_result',)
translator.register(DeclarationContract, DeclarationContractTranslationOptions)

class DeclarationDepositTranslationOptions (TranslationOptions):
    fields = ('name', 'bank', 'type', 'balance',)
translator.register(DeclarationDeposit, DeclarationDepositTranslationOptions)

class DeclarationEntrepreneurialTranslationOptions (TranslationOptions):
    fields = ('name', 'corp_name_addr', 'particn_type', 'register_agency', 'particn_date', 'income_rec',)
translator.register(DeclarationEntrepreneurial, DeclarationEntrepreneurialTranslationOptions)

class DeclarationFamilyTranslationOptions (TranslationOptions):
    fields = ('name', 'surname', 'pob', 'dob', 'relation',)
translator.register(DeclarationFamily, DeclarationFamilyTranslationOptions)

class DeclarationGiftTranslationOptions (TranslationOptions):
    fields = ('name', 'desc_value', 'giver_rel',)
translator.register(DeclarationGift, DeclarationGiftTranslationOptions)

class DeclarationOtherInclExpenseTranslationOptions (TranslationOptions):
    fields = ('recip_issuer', 'type', 'amount',)
translator.register(DeclarationOtherInclExpense, DeclarationOtherInclExpenseTranslationOptions)

class DeclarationPropertyTranslationOptions (TranslationOptions):
    fields = ('name_shares', 'prop_type', 'description', 'co_owners',)
translator.register(DeclarationProperty, DeclarationPropertyTranslationOptions)

class DeclarationRealEstateTranslationOptions (TranslationOptions):
    fields = ('name_shares', 'prop_type', 'loc_area', 'co_owners',)
translator.register(DeclarationRealEstate, DeclarationRealEstateTranslationOptions)

class DeclarationSecurityTranslationOptions (TranslationOptions):
    fields = ('name', 'issuer', 'type', 'price', 'quantity',)
translator.register(DeclarationSecurity, DeclarationSecurityTranslationOptions)

class DeclarationWageTranslationOptions (TranslationOptions):
    fields = ('name', 'desc_workplace', 'desc_job', 'income_rec',)
translator.register(DeclarationWage, DeclarationWageTranslationOptions)



from basic.blog.models import Category, Post, BlogRoll

class CategoryTranslationOptions (TranslationOptions):
    fields = ('title',)
translator.register(Category, CategoryTranslationOptions)

class PostTranslationOptions (TranslationOptions):
    fields = ('title', 'body', 'tease',)
translator.register(Post, PostTranslationOptions)

class BlogRollTranslationOptions (TranslationOptions):
    fields = ('name',)
translator.register(BlogRoll, BlogRollTranslationOptions)

