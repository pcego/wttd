from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):


    def setUp(self):
        data = dict(name='Paulo Cesar', cpf='12345678901',email='pcego36@gmail.com', phone='38-32122980')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]


    def test_subscribe_email_subject(self):
        """
        Test email subject
        """
        expect = 'Confirmacao de Inscricao'
        self.assertEqual(expect, self.email.subject)


    def test_subscription_email_from(self):
        """
        Test email from
        """
        expect = 'pcego36@gmail.com'
        self.assertEqual(expect, self.email.from_email)


    def test_subscription_email_to(self):
        """
        Test email to
        """
        expect = ['pcego36@gmail.com', 'pcego36@gmail.com']
        self.assertEqual(expect, self.email.to)


    def test_subscription_email_body(self):
        """
        Test email body
        """
        contents = ['Paulo Cesar',
                    '12345678901',
                    'pcego36@gmail.com',
                    '38-32122980']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)