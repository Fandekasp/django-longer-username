from django.contrib.auth.models import User
from django.test import TestCase

class LongerUsernameTests(TestCase):
    """
    Unit tests for longerusername app
    """

    def testUserCreation(self):
        """
        tests that User.username field has now a max_length = 255 instead of the django default 30
        """
        self.assertEqual(User._meta.get_field('username').max_length, 255,
        msg='user.signals changed the max_length from 30 to 255')