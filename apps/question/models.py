# vim: set fileencoding=utf-8
"""
Model question

Depends on representative.
"""
__docformat__ = 'epytext en'

import urllib, urllib2, copy, datetime
from cms.models.pluginmodel import CMSPlugin
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Context, loader
from django.utils.translation import ugettext as _

from settings import QUESTION_SMS_URL
from representative.models import Representative



#: URL where to send question to @ parliament.ge
URL_SEND_PARLIAMENT = 'http://parliament.ge/index.php?option=com_dmaskinfopopup'
#: map representative id @ shenmartav.ge to parliament.ge article id
SHENMARTAV2PARLIAMENT = {
    '15': '16', # Akaki Bobokhidze
    '89': '96', # Akaki Minashvili
    '2': '4', # Andro Alavidze
    '16': '17', # Anzor Bolkvadze
    '23': '36', # Archil Gegenava
    '8': '10', # Armenak Bainduriani
    '43': '123', # Aslan Tavdgiridze
    '72': '79', # Avtandil Lekashvili
    '103': '116', # Avtandil Sturua
    '104': '118', # Azer Suleimanovi
    '11': '13', # Badri Basishvili
    '19': '19', # Bezhan Butskhrikidze
    '132': '64', # Bezhan Khurtsidze
    '46': '119', # Chiora Taktakishvili
    '12': '11', # Davit Bakradze
    '14': '15', # Davit Bezhuashvili
    '125': '23', # Davit Chavchanidze
    '37': '26', # Davit Darchiashvili
    '86': '89', # Davit Makhniashvili
    '92': '99', # Davit Nadashvili
    '49': '126', # Davit Todradze
    '95': '104', # Devi Ovashvili
    '128': '60', # Dilar Khabuliani
    '76': '83', # Dimitri Lortkipanidze
    '135': '50', # Edisher Jalaghonia
    '130': '62', # Ekaterine Kherkheulidze
    '61': '76', # Eldar Kvernadze
    '134': '52', # Elene Javakhadze
    '79': '88', # Elguja Makaradze
    '25': '37', # Emzar Gelashvili
    '91': '98', # Enzel Mkoiani
    '75': '82', # Gela Londaridze
    '29': '43', # Gia Goguadze
    '53': '130', # Gia Tortladze
    '6': '2', # Giorgi Akhvlediani
    '5': '7', # Giorgi Asanidze
    '126': '24', # Giorgi Chelidze
    '20': '33', # Giorgi Gabashvili
    '44': '122', # Giorgi (Givi) Targamadze
    '31': '40', # Giorgi Godabrelidze
    '30': '44', # Giorgi Goguadze
    '32': '45', # Giorgi Gugava
    '54': '48', # Giorgi Imnadze
    '56': '54', # Giorgi Kandelaki
    '129': '61', # Giorgi Khakhnelidze
    '87': '94', # Giorgi Meladze
    '99': '107', # Giorgi Roinishvili
    '107': '120', # Giorgi Talakhadze
    '45': '121', # Giorgi Targamadze
    '118': '131', # Giorgi Tsagareishvili
    '122': '132', # Giorgi Tsereteli
    '39': '31', # Gocha Enukidze
    '69': '72', # Gocha Kuprava
    '113': '112', # Gocha Shanidze
    '48': '125', # Gocha Tevdoradze
    '18': '18', # Goderdzi Bukia
    '74': '81', # Gogi Liparteliani
    '117': '21', # Guram Chakhvadze
    '55': '53', # Guram Kakalashvili
    '133': '49', # Guranda Jabua
    '137': '47', # Harutiun Hovhanesyan
    '115': '114', # Iasha Shervashidze
    '114': '113', # Ioseb Shatberashvili
    '109': '55', # Irakli Kavtaradze
    '58': '57', # Irakli Kenchoshvili
    '112': '111', # Isvakhan Shamilov
    '84': '86', # Jaba Maghlakelidze
    '13': '9', # Jondo Baghaturia
    '4': '5', # Kakhaber Anjaparidze
    '121': '30', # Kakhaber Dzagania
    '96': '103', # Kakhaber Okriashvili
    '105': '117', # Kakhaber Sukhishvili
    '26': '39', # Kakha Getsadze
    '62': '77', # Kandid Kvitsiani
    '64': '68', # Karlo Kopaliani
    '28': '42', # Khatuna Gogorishvili
    '97': '102', # Khatuna Ochiauri
    '7': '8', # Koba Badagadze
    '127': '59', # Koba Khabazi
    '70': '73', # Koba Kurdghelashvili
    '94': '100', # Koba Nakopia
    '68': '71', # Korneli Kukulava
    '36': '25', # Lasha Damenia
    '90': '97', # Lasha Mindeli
    '52': None, # Lasha Tordia
    '42': '137', # Levan Vepkhvadze
    '3': '6', # Magdalina Anikashvili
    '22': '34', # Mamuka Gachechiladze
    '27': '41', # Mamuka Gogatishvili
    '102': '110', # Mamuka Saneblidze
    '41': '138', # Marika Verulashvili
    '100': '108', # Merab Samadashvili
    '85': '84', # Mikheil Machavariani
    '120': '135', # Mikheil Tskitishvili
    '136': '51', # Naul Janashia
    '71': '78', # Nikoloz Laliashvili
    '1': '3', # Nugzar Abulashvili
    '40': '32', # Nugzar Ergemlidze
    '123': '133', # Nugzar Tsiklauri
    '131': '63', # Otar Khinikadze
    '51': '128', # Otar Toidze
    '34': '27', # Paata Davitaia
    '73': '80', # Paata Lezhava
    '66': '69', # Pavle Kublashvili
    '81': '91', # Petre Mamradze
    '119': '134', # Petre Tsiskarishvili
    '50': '127', # Pridon Todua
    '47': '124', # Ramaz Tedoradze
    '9': '14', # Ramin Bayramov
    '78': '87', # Rati Maisuradze
    '101': '109', # Rati Samkurashvili
    '57': '56', # Roland Kemularia
    '108': '106', # Roland Pipia
    '82': '92', # Roman Marsagishvili
    '17': '20', # Romanoz Bzhalava
    '59': '58', # Rusudan Kervalishvili
    '111': '74', # Samson Kutateladze
    '110': '66', # Sergo Kitiashvili
    '93': '101', # Shalva Natelashvili
    '80': '90', # Shota Malashkhia
    '38': '29', # Tamaz Diasamidze
    '60': '75', # Tamaz Kvachantiradze
    '98': '105', # Tamaz Petriashvili
    '116': '22', # Teimuraz Charkviani
    '124': '136', # Teimuraz Tsurtsumia
    '65': '67', # Temur Kokhodze
    '106': '115', # Tengiz Shkhirtladze
    '10': '12', # Vakhtang Balavadze
    '83': '93', # Vakhtang Martoleki
    '35': '28', # Vasil Davitashvili
    '21': '35', # Zaal Gamtsemlidze
    '24': '38', # Zaza Gelashvili
    '33': '46', # Zaza Gulikashvili
    '77': '85', # Zaza Madurashvili
    '63': '65', # Zurab Kikaleishvili
    '88': '95', # Zurab Melikishvili
    '67': '70', # Zviad Kukava
}



class PublicManager (models.Manager):
    """Manager to return public questions."""
    def _clone(self): # bug in Manager? DetailView complains about it missing
        return copy.copy(self)

    def get_query_set(self):
        qs = super(PublicManager, self).get_query_set()
        return qs.filter(is_public=True)



class AnsweredManager (models.Manager):
    """Manager to return answered public questions."""
    def get_query_set(self):
        qs = super(AnsweredManager, self).get_query_set()
        return qs.filter(answer__isnull=False).exclude(answer__exact='')



class Question (models.Model):
    """A question."""
    #: if question is public
    is_public = models.BooleanField(default=False, help_text=_('Is this question public?'))
    #: when the question was asked
    date = models.DateField(default=datetime.datetime.now, help_text=_('When Question was asked'))
    #: first name of the questioner
    first_name = models.CharField(max_length=255, verbose_name=_('First Name'), help_text=_('First Name of the Questioner'))
    #: last name of the questioner
    last_name = models.CharField(max_length=255, verbose_name=_('Last Name'), help_text=_('Last Name of the Questioner'))
    #: email address of the questioner
    email = models.CharField(max_length=255, verbose_name=_('Email Address'), help_text=_('Email Address of the Questioner'))
    #: mobile phone number of the questioner
    mobile = models.CharField(blank=True, max_length=255,
        verbose_name=_('Mobile Phone Number'),
        help_text=_('Mobile Phone Number of the Questioner'))
    #: the actual question
    question = models.TextField(verbose_name=_('Question'), help_text=_('The Question'))
    #: the representative being asked
    representative = models.ForeignKey(Representative,
        related_name='questions', verbose_name=_('Representative'),
        help_text=_('Representative being asked'))
    #: the representative's answer
    answer = models.TextField(help_text=_('The Answer'), blank=True, null=True)
    #: parliament.ge response
    parliament_response = models.TextField(blank=True, null=True,
        help_text=_('Response from parliament.ge when sending the question'))

    #: managers
    objects = models.Manager()
    public = PublicManager()
    answered = AnsweredManager()


    class Meta:
        ordering = ['-date', 'is_public']


    @property
    def name (self):
        return self.first_name + ' ' + self.last_name


    def __unicode__ (self):
        try:
            return u'%s %s -> %s: %s' % (self.date, self.name,
                self.representative.name, self.question[:30])
        except Representative.DoesNotExist:
            return u'%s %s -> %s' % (self.date, self.name, self.question[:30])


    @models.permalink
    def get_absolute_url (self, language=None):
        return ('question_detail', [self.pk])


    def _notify_questioner (self):
        """Send a notification to questioner."""
        if self.email:
            subject = _('%(name_asker)s, your question to %(name_representative)s has been answered.' % {
                'name_asker': self.name,
                'name_representative': self.representative.name}
            )
            body = self.question + '\n\n' + self.answer
            msg = EmailMessage(subject=subject, body=body, to=(self.email,))
            msg.send()

        if self.mobile:
            url = QUESTION_SMS_URL.replace('to=', 'to=' + self.mobile).replace(
                'msg=', 'msg=' + urllib2.quote(self.answer))
            try:
                handle = urllib2.urlopen(url)
                response = handle.read()
                handle.close()
            except urllib2.URLError, err:
                pass # silently ignore for the time being
#            else:
#                print 'Response: %s' % response


    def _set_percentage_answered (self):
        """Sets the percentage of questions answered by self's representative."""
        pk = self.representative.pk
        total = Question.public.filter(representative=pk).count()
        two_weeks_ago = datetime.date.today() - datetime.timedelta(14)
        answered = Question.answered.filter(
            representative=pk, date__lt=two_weeks_ago).count()

        try:
            self.representative.answered = (answered * 100.) / total
        except ZeroDivisionError:
            self.representative.answered = 0.
        self.representative.save()


    def _copy_formdata (self):
        """
        Copies data supplied in Ask form to language-specific fields on
        first save (pk doesn't exist).
        """
        if not self.pk:
            self.first_name_en = self.first_name_ka = self.first_name
            self.last_name_en = self.last_name_ka = self.last_name
            self.question_en = self.question_ka = self.question


    def save (self, *args, **kwargs):
        try:
            saved = Question.objects.get(pk=self.pk)
            if saved.answer != self.answer and self.answer:
                self._notify_questioner()
        except Question.DoesNotExist:
            pass

        self._copy_formdata()
        super(Question, self).save(*args, **kwargs)

        if self.is_public:
            self._set_percentage_answered()



def _get_send_data (question, arid):
    """Get data to be sent to parliament.ge.

    @param question: question to be asked
    @type question: question.Question
    @param arid: article (representative) id
    @type arid: str
    @return: urlencoded send data
    @rtype: str
    """
    site = Site.objects.get_current()
    representative = question.representative
    sender_id = representative.slug + '-' + str(question.pk)
    sender = 'ask+' + sender_id + '@' + site.domain
    user_name = question.first_name + ' ' + question.last_name

    subject = u'თქვენ დაგისვეს შეკითხვა ShenMartav.ge-ზე'
    # temporarily disable template
    #template = loader.get_template('question/send_parliament.html')
    #context = Context({
    #    'gender': representative.gender,
    #    'first_name': str(representative.name).split()[0],
    #    'user_name': user_name,
    #    'question': question.question,
    #})
    #message = template.render(context)
    message = question.question

    # urllib.urlencode needs UTF-8 bytecode to URL-encode
    values = {
        'mail' : sender,
        'name' : user_name.encode('utf-8'),
        'subj' : subject.encode('utf-8'),
        'mess' : message.encode('utf-8'),
        'arid': arid,
        'adminemail' : '-1',
        'extrafield' : '',
        'extrafield2' : '',
        'extrafield3' : '',
        'component' : 'com_k2',
    }
    data = urllib.urlencode(values)

    return data

@receiver(post_save, sender=Question, dispatch_uid='apps.question.post_save.send_parliament')
def send_parliament (sender, **kwargs):
    """Send a question to parliament(arian).

    CAREFUL: it is executed on Question.post_save and calls Question.save if
    public and no parliament_response is set. Might be a cause for infinite
    loops.
    """
    question = kwargs['instance']
    if not question.is_public or question.parliament_response:
        return

    try:
        arid = SHENMARTAV2PARLIAMENT[str(question.representative.pk)]
    except KeyError:
        arid = None

    response = []
    if arid:
        data = _get_send_data(question, arid)
        req = urllib2.Request(URL_SEND_PARLIAMENT, data)
        try:
            opened = urllib2.urlopen(req)
            response += [
                'RESPONSE CODE: ' + str(opened.getcode()),
                'RESPONSE CONTENT: ' + opened.read(),
            ]
        except urllib2.URLError, err:
            response += [
                'URL ERROR: ' + str(err),
                'URL: ' + URL_SEND_PARLIAMENT,
            ]
        response.append('SENT DATA LENGTH: ' + str(len(data)))
        response.append('SENT DATA: ' + data)
    else:
        name = str(question.representative.name)
        response.append('No arid @ parliament.ge for representative %s' % name)

    question.parliament_response = '\n'.join(response)
    question.save()



# There must be a bug in CMS plugin models. Without exception handler, on
# running an admin command, the class definition would yield:
#  File "/votingrecord/models.py", line 70, in <module>
#      class VotingRecordPluginConf (CMSPlugin):
#        File "/usr/local/lib/python2.7/dist-packages/cms/models/pluginmodel.py", line 56, in __new__
#            table_name = 'cmsplugin_%s' % splitted[1]
#            IndexError: list index out of range
try:
    class QuestionPluginConf (CMSPlugin):
        """Configuration for voting record plugin."""
        #: title of the plugin
        title = models.CharField(max_length=32, default=_('Questions'))
except IndexError:
    pass
