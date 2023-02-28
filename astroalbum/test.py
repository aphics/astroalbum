from django.test import TestCase
from .register_validator import user_validator, password_validator

# Create your tests here.

class TestUserPasswordValidator(TestCase):

    def setUp(self):
        self.username1 = 'Edgar'
        self.username2 = 'EdgarONE'
        
        self.password1 = 'Password'
        self.password2 = '12345'
        self.password3 = 'password'
        self.password4 = 'Pass1'
        self.password5 = 'Password10'
    
    def test_user_validator(self):
        self.assertFalse(user_validator(self.username1))
        self.assertTrue(user_validator(self.username2))
    
    def test_password_validator(self):
        self.assertFalse(password_validator(self.password1))
        self.assertFalse(password_validator(self.password2))
        self.assertFalse(password_validator(self.password3))
        self.assertFalse(password_validator(self.password4))
        self.assertTrue(password_validator(self.password5))

