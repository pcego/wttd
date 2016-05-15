from django.test import TestCase

class SubscribeTest(TestCase):

    """
    GET /inscricao/ must return status code 200
    """
    def test_get(self):
        response = self.client.get('/inscricao/')
        self.assertEqual(200, response.status_code)

    def test_template(self):
        """
        MUST use subscritions/subscriptions_form.html
        """
        response = self.client.get('/incricao/')
        self.assertTemplateUsed(response, 'subscriptions/subscription_form.html')