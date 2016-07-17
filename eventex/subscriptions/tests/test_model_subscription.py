from datetime import datetime
from django.shortcuts import resolve_url as r
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):

    def setUp(self):

        self.obj = Subscription(
                name='Paulo Cesar',
                cpf='12345678901',
                email='pcego36@gmail.com',
                phone='38-3212-2980',
            )

        self.obj.save()

    def test_create(self):

        self.assertTrue(Subscription.objects.exists())

    def test_creat_at(self):
        """
        Subscription must have an auto create at atr
        """
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Paulo Cesar', str(self.obj))


    def test_paid_default_to_false(self):
        """by default paid must be false"""

        self.assertEqual(False, self.obj.paid)


    def test_get_absolute_url(self):
        url = r('subscriptions:detail', self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())