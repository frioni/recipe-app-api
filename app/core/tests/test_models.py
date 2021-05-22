from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_mail(self):
        """Test creation of new user with mail"""
        email = 'test@mail.com'
        password = 'password123'
        user = get_user_model() \
            .object \
            .create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """test new user mail normalization"""
        mail = 'user@MAIL.com'
        user = get_user_model() \
            .object \
            .create_user(email=mail, password='password')
        self.assertEqual(user.email, mail.lower())

    def test_user_invalid_mail(self):
        """creating user with no valid mail will raise error"""
        with self.assertRaises(ValueError):
            get_user_model().object.create_user(None, 'pass')

    def test_create_superuser(self):
        """creating super user"""
        user = get_user_model().object.create_superuser('super@user', 'passw')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
