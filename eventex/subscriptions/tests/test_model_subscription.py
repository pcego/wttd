from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):

    def setUp(self):

        self.obj = Subscription(
                name='Paulo César',
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