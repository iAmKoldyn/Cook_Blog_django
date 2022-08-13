from django.test import TestCase

from .models import Customer

# Create your tests here.

OK = 200

class MainPageTestSet(TestCase):
    
    def main_in_desired_location(self):
        resp = self.customer.get('')
        self.assertEqual(resp.status_code, OK)
