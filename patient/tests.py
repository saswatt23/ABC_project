from django.test import TestCase
from .models import Patient

class PatientTestCase(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            user__username='test_patient',  # Creating a related user
            age=30,
            bloodgroup='AB+',
            disease='Test Disease',
            doctorname='Dr. Test',
            address='Test Address',
            mobile='1234567890'
        )

    def test_get_name(self):
        self.assertEqual(self.patient.get_name, 'Test Patient')  # Assuming user has first and last names

    def test_str_representation(self):
        self.assertEqual(str(self.patient), 'Test Patient')

    # Add more test methods as needed
