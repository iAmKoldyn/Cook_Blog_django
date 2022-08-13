from django.test import TestCase

# Create your tests here.
from blog.models import Customer


# Create your tests here.

OK = 200

class ContactTestSet(TestCase):

    def contact_in_desired_location(self):
        resp = self.customer.get('/contact/')
        self.assertEqual(resp.status_code, OK)

class AboutTestSet(TestCase):
    
    def about_in_desired_location(self):
        resp = self.customer.get('/about/')
        self.assertEqual(resp.status_code, OK)

class RegisterTestSet(TestCase):
    
    def register_in_desired_location(self):
        resp = self.customer.get('/register/')
        self.assertEqual(resp.status_code, OK)
    
class LoginTestSet(TestCase):
    
    def login_in_desired_location(self):
        resp = self.customer.get('/login/')
        self.assertEqual(resp.status_code, OK)

class LogoutTestSet(TestCase):
    def logout_in_desired_location(self):
        resp = self.customer.get('/logout/')
        self.assertEqual(resp.status_code, OK)