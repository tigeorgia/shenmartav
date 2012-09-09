# -*- coding: utf-8 -*
"""
Views question

Depends on representative.
"""
__docformat__ = 'epytext en'

import datetime, urllib, urllib2, socket

from django.contrib.sites.models import Site
from django.core.mail import mail_managers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views.generic import DetailView, ListView, FormView, TemplateView
try:
    from menus.utils import set_language_changer
except ImportError:
    from cms.utils import set_language_changer

try:
    from settings import QUESTION_SMS_EMAIL
except ImportError:
    QUESTION_SMS_EMAIL = 'root@localhost'

from representative.models import Representative

from .models import Question
from .forms import QuestionForm


#: pagination value
PAGINATE_BY = 30

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


def _get_form (view, representative=None):
    """Get question form for given representative.

    @param view: view object
    @type view: generic view
    @param representative: representative to get form for
    @type representative: representative.Representative
    @return: question form for given representative
    @type: QuestionForm
    """
    if representative:
        if 'form_question' in view.request.session:
            view.request.session['form_question']['representative'] =\
                representative.pk
        else:
            view.request.session['form_question'] = {
                'representative': representative.pk
            }

    return QuestionForm(session=view.request.session)



def notify_question_change (pk, question):
    """Notify site managers of a new/changed question.

    @param pk: primary key of the question
    @type pk: int
    @param question: question being asked
    @type question: str
    """
    subject = _('New question: %d') % pk

    uri = reverse('admin:question_question_change', args=(pk,))
    if uri.startswith('/mapit'): # err... FIXME?
        uri = uri[6:]
    site = Site.objects.get_current()
    message = _('%(question)s\n\nPlease manage at http://%(domain)s%(uri)s' % {
        'question': question,
        'domain': site.domain,
        'uri': uri}
    )

    try:
        mail_managers(subject, message)
    except socket.error: # silently ignore if mail system not setup, e.g. localhost
        pass


def send_parliament (question):
    """Send a question to parliament(arian).

    @param question: question object
    @type question: question.Question
    """
    try:
        arid = SHENMARTAV2PARLIAMENT[str(question.representative.pk)]
    except KeyError:
        arid = None

    if arid:
        url = 'http://parliament.ge/index.php?option=com_dmaskinfopopup'
        values = {
            'mail' : 'question-' + str(question.pk) + '@shenmartav.ge',
            'name' : question.first_name + ' ' + question.last_name,
            'subj' : question.question[:32] + ' ...',
            'mess' : question.question,
            'arid': arid,
            'adminemail' : '-1',
            'extrafield' : '',
            'extrafield2' : '',
            'extrafield3' : '',
            'component' : 'com_k2',
        }
        data = urllib.urlencode(values)

        req = urllib2.Request(url, data)
        try:
            opened = urllib2.urlopen(req)
            response = str(opened.getcode()) + '\n\n' + opened.read()
        except urllib2.URLError, err:
            response = str(err) + '\n\n' + url
    else:
        name = str(question.representative.name)
        response = 'No arid @ parliament.ge for representative %s' % name

    question.parliament_response = response
    question.save()



class List (ListView):
    """Implements the Question list view."""
    template_name = 'question/list.html'
    model = Question
    queryset = Question.public.order_by('-date')


    def get_context_data (self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        context['form'] = _get_form(self)
        context['url_feed'] = reverse('question_feed_list')
        return context



class Ask (FormView):
    """Implements the Question ask view."""
    template_name = 'question/ask.html'
    form_class = QuestionForm


    def form_valid (self, form):
        obj = form.save()

        # at some stage it might be wise to have these added to a queueing
        # system (celery? rabbitmq?)
        send_parliament(obj)
        notify_question_change(obj.pk, obj.question)

        self.request.session['form_question'] = {
            'representative': obj.representative.pk,
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'email': obj.email,
            'mobile': obj.mobile,
        }

        return redirect('question_thanks')


    def form_invalid (self, form):
        return self.render_to_response({'form': form})


    def get_context_data (self, **kwargs):
        context = super(Ask, self).get_context_data(**kwargs)

        if 'pk' in self.kwargs: # from query params
            if 'form_question' in self.request.session:
                self.request.session['form_question']['representative'] =\
                    self.kwargs['pk']
            else:
                self.request.session['form_question'] = {
                    'representative': self.kwargs['pk']
                }

        question = context['form'].instance
        context['form'] = QuestionForm(instance=question,
            session=self.request.session)
        context['url_feed'] = reverse('question_feed_list')

        return context



class Thanks (TemplateView):
    """Implements the Question thanks view."""
    template_name = 'question/thanks.html'

    def get_context_data (self, **kwargs):
        context = super(Thanks, self).get_context_data(**kwargs)

        if 'form_question' in self.request.session:
            context['representative'] =\
                self.request.session['form_question']['representative']
        context['url_feed'] = reverse('question_feed_list')

        return context


class Detail (DetailView):
    """Implements the Question detail view."""
    context_object_name = 'obj'
    model = Question
    queryset = Question.public
    slug_field = 'pk'
    template_name = 'question/detail.html'


    def get_context_data (self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        context['form'] = _get_form(self, context['obj'].representative)
        context['url_feed'] = reverse('question_feed_list')
        set_language_changer(self.request, context['obj'].get_absolute_url)

        return context



class Leaderboard (ListView):
    """Shows a leaderboard of representatives by questions answered."""
    model = Representative
    queryset = Representative.objects.filter(questions__is_public=True,
        questions__isnull=False).distinct().order_by('-answered')
    template_name = 'question/leaderboard.html'


    def get_context_data (self, **kwargs):
        context = super(Leaderboard, self).get_context_data(**kwargs)
        context['url_feed'] = reverse('question_feed_list')
        return context



class Info (DetailView):
    context_object_name = 'obj'
    model = Question
    queryset = Question.public
    template_name = 'question/info.html'


    def get_context_data (self, **kwargs):
        context = super(Info, self).get_context_data(**kwargs)
        return context



class Items (TemplateView):
    """Implements a view with paged question items."""
    template_name = 'question/items.html'


    def _add_item_states (self, page):
        """Set item states in given page.

        @param page: page number to retrieve
        @type page: int
        @return: a page with questions
        @rtype: Paginator.page
        """
        if not page:
            return None

        two_weeks_ago = datetime.date.today() - datetime.timedelta(14)
        answered = { 'text': 'answered', 'value': 2 }
        unanswered_new = { 'text': 'unanswered-new', 'value': 1 }
        unanswered_old = { 'text': 'unanswered-old', 'value': 0 }

        for item in page.object_list:
            if item.answer:
                item.state = answered
            else:
                if item.date >= two_weeks_ago:
                    item.state = unanswered_new
                else:
                    item.state = unanswered_old

        return page


    def _get_items (self, page):
        """Get given queryset as page.

        @param page: page number to retrieve
        @type page: int
        @return: a page with questions
        @rtype: Paginator.page
        """
        queryset = Question.public.order_by('-date')
        paginator = Paginator(queryset, PAGINATE_BY)
        try:
            result = paginator.page(page)
        except (PageNotAnInteger, TypeError):
            result = paginator.page(1)
        except EmptyPage:
            result = None
        #    result = paginator.page(paginator.num_pages)

        return self._add_item_states(result)


    def get_context_data (self, **kwargs):
        context = super(Items, self).get_context_data(**kwargs)
        context['items'] = self._get_items(context['params']['page'])
        return context



def receive (request, mobile, representative, question):
    """Receive questions from sms server.

    @param mobile: mobile phone number of the asker
    @type mobile: str
    @param representative: id of the representative to ask
    @type representative: int
    @param question: question asked
    @type question: str
    @return: response, either 'Bad data' or 'OK'
    @rtype: HttpResponse
    """
    try:
        question = Question(representative_id=representative,
            name=_('SMS'), email=QUESTION_SMS_EMAIL, mobile=mobile, question=question,
        )
        question.save()
    except (ValueError, IntegrityError):
        return HttpResponseBadRequest('Bad data')

    notify_question_change(question.pk, question.question)
    return HttpResponse('OK')
