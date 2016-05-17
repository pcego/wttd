from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):

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
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

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

    def test_have_fields(self):
        """
        Form must have for fields
        """
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cpf','email', 'phone'], list(form.fields))

class SubscribePostTest(TestCase):

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

    def test_subscribe_email_subject(self):
        """
        Test email subject
        """
        email = mail.outbox[0]
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, email.subject)

    def test_subscription_email_from(self):
        """
        Test email from
        """
        email = mail.outbox[0]
        expect = 'pcego36@gmail.com'
        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        """
        Test email to
        """
        email = mail.outbox[0]
        expect = ['contato@eventex.com.br', 'pcego36@gmail.com']
        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        """
        Test email body
        """
        email = mail.outbox[0]
        self.assertIn('Paulo César', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('pcego36@gmail.com', email.body)
        self.assertIn('38-32122980', email.body)

class SubscribeInvalidPost(TestCase):

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

class SubscribeSucessMessage(TestCase):
    """
    Test message sucess for user
    """
    def test_message(self):
        data = dict(name='Paulo César', cpf='12345678901',
                    email='pcego36@gmail.com', phone='38-3212-2980')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição Realizada com Sucesso!')