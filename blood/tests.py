from django.test import TestCase
from .models import Stock, BloodRequest

class YourAppTestCase(TestCase):
    def setUp(self):
        # Create test instances of your models for use in the tests
        Stock.objects.create(bloodgroup='A+', unit=10)
        BloodRequest.objects.create(
            patient_name='John Doe', patient_age=30, reason='Emergency', bloodgroup='B+', unit=2, status='Pending'
        )

    def test_stock_creation(self):
        # Test that a stock instance was created successfully
        stock = Stock.objects.get(bloodgroup='A+')
        self.assertEqual(stock.unit, 10)

    def test_blood_request_creation(self):
        # Test that a blood request instance was created successfully
        request = BloodRequest.objects.get(patient_name='John Doe')
        self.assertEqual(request.bloodgroup, 'B+')

    # Add more test methods as needed

