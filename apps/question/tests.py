# -*- coding: utf-8 -*
"""
Tests for app question
"""
__docformat__ = 'epytext en'

from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from question.models import Question
from question.views import notify_question_change, Items


class QuestionTest (TestCase):
    fixtures = ['question_testdata']
    # problem with urls not available in cms apps, so this apps' URLCONF has to
    # be added in ROOT_URLCONF
    # urls = 'question.urls'

    def test_PublicManager (self):
        obj = Question.public.all()[0]
        self.assertEqual(obj.is_public, True)


    def test_unicode (self):
        obj = Question.objects.all()[0]
        self.assertEqual(str(obj), "2012-06-05 test site -> \xe1\x83\x90\xe1\x83\x91\xe1\x83\xa3\xe1\x83\x9a\xe1\x83\x90\xe1\x83\xa8\xe1\x83\x95\xe1\x83\x98\xe1\x83\x9a\xe1\x83\x98 \xe1\x83\x9c\xe1\x83\xa3\xe1\x83\x92\xe1\x83\x96\xe1\x83\x90\xe1\x83\xa0\xe1\x83\x98: how's things in Foobar?")


    def test_notify_questioner (self):
        obj = Question.objects.all()[0]
        # assert answer exists
        obj.answer = 'answer'
        obj._notify_questioner()

        self.assertEqual(len(mail.outbox), 1)
        msg = mail.outbox[0]
        self.assertEqual(msg.subject, u'test site, your question to აბულაშვილი ნუგზარი has been answered.')
        self.assertEqual(msg.to, [u'foo@bar.com'])
        self.assertEqual(msg.body, "how's things in Foobar?\n\nanswer")


    def test_set_percentage_answered (self):
        obj = Question.public.all()[0]
        previous = obj.representative.answered
        obj.answer = 'answer'
        obj.save()
        self.assertNotEqual(obj.representative.answered, previous)

        obj = Question.public.all()[1]
        previous = obj.representative.answered
        obj.save()
        self.assertEqual(obj.representative.answered, previous)


    def test_List (self):
        url = reverse('question_list')
        response = self.client.get(url)
        self.assertContains(response, 'question')
        self.assertTemplateUsed(response, 'question/list.html')


    def test_Ask (self):
        url = reverse('question_ask')
        response = self.client.get(url)
        self.assertContains(response, 'question')
        self.assertTemplateUsed(response, 'question/ask.html')


        postdata = {
            'first_name': 'foo',
            'last_name': 'bar',
            'email': 'foo@bar.com',
            'question': 'question',
            'representative': 1
        }
        response = self.client.post(url, postdata, follow=True)
        self.assertEqual(self.client.session['form_question'], {
            'mobile': u'',
            'first_name': u'foo',
            'last_name': u'bar',
            'representative': 1,
            'email': u'foo@bar.com'
        })
        self.assertContains(response, 'question')
        self.assertTemplateUsed(response, 'question/thanks.html')


    def test_AskRepresentative (self):
        url = reverse('question_ask_representative', args=[1])
        response = self.client.get(url)
        self.assertContains(response, 'question')
        self.assertTemplateUsed(response, 'question/ask.html')


    def test_Thanks (self):
        url = reverse('question_thanks')
        response = self.client.get(url)
        self.assertContains(response, 'question')
        self.assertTemplateUsed(response, 'question/thanks.html')


    def test_Leaderboard (self):
        url = reverse('question_leaderboard')
        response = self.client.get(url)
        self.assertContains(response, 'question')
        self.assertTemplateUsed(response, 'question/leaderboard.html')


    def test_Info (self):
        url = reverse('question_info', args=[2])
        response = self.client.get(url)
        self.assertContains(response, 'the-question')
        self.assertTemplateUsed(response, 'question/info.html')


    def test_Items (self):
        url = reverse('question_items', args=[1])
        response = self.client.get(url)
        self.assertContains(response, 'question')
        self.assertTemplateUsed(response, 'question/items.html')


    def test_get_items (self):
        item = Items()
        objs = item._get_items(1).object_list
        self.assertEqual(len(objs), 6)


    def test_Detail (self):
        url = reverse('question_detail', args=[2])
        response = self.client.get(url)
        self.assertContains(response, 'question')
        self.assertTemplateUsed(response, 'question/detail.html')


    def test_receive (self):
        url = reverse('question_receive', args=[
            '110', 1, 'question'
        ])
        response = self.client.get(url)
        self.assertContains(response, 'OK')

        # can't figure out how to provoke this, but Bad data did happen
        #url = reverse('question_receive', args=[
        #    '110', 1, 'this is the question'
        #])
        #response = self.client.get(url)
        #self.assertContains(response, 'Bad data')


    def test_notify_question_change (self):
        obj = Question.public.all()[0]
        notify_question_change(obj.pk, obj.question)

        self.assertEqual(len(mail.outbox), 1)
        msg = mail.outbox[0]
        self.assertEqual(msg.subject, u'[ShenMartav] \u10d0\u10ee\u10d0\u10da\u10d8 \u10e8\u10d4\u10d9\u10d8\u10d7\u10ee\u10d5\u10d0: 2')
        self.assertEqual(msg.to, [u'sebastian@transparency.ge'])
        self.assertEqual(msg.body, u'blabla\n\nPlease manage at http://example.com/admin/question/question/2/')

