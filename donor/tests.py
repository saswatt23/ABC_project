from django.test import TestCase
from django.contrib.auth.models import User
from .models import Donor

class DonorTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(
            username='test_user', password='password123', first_name='John', last_name='Doe'
        )
        
        # Create a test donor
        self.test_donor = Donor.objects.create(
            user=self.test_user, bloodgroup='O+', address='Test Address', mobile='1234567890'
        )

    def test_get_name(self):
        # Test the get_name property of the Donor model
        self.assertEqual(self.test_donor.get_name, 'John Doe')

    def test_str_representation(self):
        # Test the __str__ method of the Donor model
        self.assertEqual(str(self.test_donor), 'John')

    # Add more test methods as needed

