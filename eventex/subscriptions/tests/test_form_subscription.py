from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):


    def test_have_fields(self):
        """
        Form must have for fields
        """
        form = SubscriptionForm()
        expected = ['name', 'cpf','email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))


    def test_cpf_is_digit(self):

        """
        cpf must only accept digits
        """
        form = self.make_validated_form(cpf='abc12345680')
        self.assertFormErrorCode(form, 'cpf', 'digits')


    def test_cpf_has_11_digits(self):

        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')


    def test_name_must_be_capitalized(self):
        """
        Name must be Capitalized
        """
        form = self.make_validated_form(name='PAULO cesar')
        self.assertEqual('Paulo Cesar', form.cleaned_data['name'])



    def assertFormErrorCode(self, form, field, code):

        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)


    def assertFormErrorMessage(self, form, field, msg):

        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)


    def make_validated_form(self, **kwargs):

        valid = dict(name='Paulo', cpf='12345678901',
                    email='pcego36@gmail.com', phone='32122980')

        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return form