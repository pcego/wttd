from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def setUp(self):
        self.form = SubscriptionForm()

    def test_have_fields(self):
        """
        Form must have for fields
        """
        expected = ['name', 'cpf','email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))