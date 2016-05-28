from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeGet(TestCase):

    def setUp(self):
        self.response = self.client.get('/inscricao/')


    def test_get(self):
        """
        GET /inscricao/ must return status code 200
        """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """
        MUST use subscritions/subscriptions_form.html
        """
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """
        HTML must contain input tags
        """
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)


    def test_csrf(self):
        """
        HTML must contain csrf
        """

        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """
        Context must have subscriptions form
        """
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Paulo César', cpf='12345678901',email='pcego36@gmail.com', phone='38-32122980')
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        """
        Valid POST should redirect to /inscricao/
        """
        self.assertEqual(302, self.response.status_code)

    def test_send_subscribe_email(self):
        """
        Test Send Email
        """
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        """
        Test save subscription on bd
        """
        self.assertTrue(Subscription.objects.exists())

class SubscribePostInvalid(TestCase):

    def setUp(self):
        self.response = self.client.post('/inscricao/', {})

    def test_post(self):

        """ Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """
        Valid template form
        """
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        """
        Test has form
        """
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        """
        Test verification form errors
        """
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        """
        Test fail save subscription on bd
        """
        self.assertFalse(Subscription.objects.exists())

class SubscribeSucessMessage(TestCase):
    """
    Test message sucess for user
    """
    def test_message(self):
        data = dict(name='Paulo César', cpf='12345678901',
                    email='pcego36@gmail.com', phone='38-3212-2980')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscricao Realizada com Sucesso!')