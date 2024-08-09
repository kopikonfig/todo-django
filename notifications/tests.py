# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\notifications\tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Notification

class NotificationModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="password")
        Notification.objects.create(user=self.user, title="Test Notification", message="This is a test message")

    def test_notification_str(self):
        notification = Notification.objects.get(title="Test Notification")
        self.assertEqual(str(notification), f"Test Notification - {self.user.username}")
