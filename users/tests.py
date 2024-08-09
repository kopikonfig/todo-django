# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\users\tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="password")
        self.profile = UserProfile.objects.create(user=self.user, full_name="Test User", phone_number="1234567890")

    def test_user_profile_str(self):
        self.assertEqual(str(self.profile), self.user.username)
