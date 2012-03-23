from django.contrib.auth.models import User
from django.test import TestCase


class LongerUsernameTests(TestCase):
    """
    Unit tests for longerusername app
    """

    def setUp(self):
        """creates a user with a terribly long username"""
        long_username = ''.join([str(i) for i  in range(100)])
        self.user = User.objects.create_user('test' + long_username,
            'test@test.com', 'testpassword')

    def test_user_creation(self):
        """
        tests that self.user was successfully saved, and can be retrieved
        """
        self.assertNotEqual(self.user,None)
        # returns DoesNotExist error if the user wasn't created
        User.objects.get(id=self.user.id)

    def test_username_max_length(self):
        """
        tests that User.username field has now a max_length = 255 instead of
        the django default 30
        """
        self.assertEqual(User._meta.get_field('username').max_length, 255,
            msg='user.signals changed the max_length from 30 to 255')
