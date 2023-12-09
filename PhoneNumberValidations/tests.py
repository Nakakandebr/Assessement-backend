from django.test import TestCase
from .models import PhoneNumber

class PhoneNumberModelTests(TestCase):
    def setUp(self):
       
        self.sample_phone_number = PhoneNumber.objects.create(
            country='Cameroon',
            state=True,
            country_code='+237',
            phone_number='123456789'
        )

    def test_phone_number_str_representation(self):
        """
        Test the __str__ method of the PhoneNumber model.
        """
        expected_str = 'Cameroon - +237 123456789'
        self.assertEqual(str(self.sample_phone_number), expected_str)

    def test_phone_number_creation(self):
        """
        Test the creation of a PhoneNumber instance.
        """
        self.assertEqual(self.sample_phone_number.country, 'Cameroon')
        self.assertTrue(self.sample_phone_number.state)
        self.assertEqual(self.sample_phone_number.country_code, '+237')
        self.assertEqual(self.sample_phone_number.phone_number, '123456789')
