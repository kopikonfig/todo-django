# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\logs\tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import LogEntry

class LogEntryModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="password")
        LogEntry.objects.create(user=self.user, action="create", description="Test log entry")

    def test_log_entry_str(self):
        log_entry = LogEntry.objects.get(action="create")
        self.assertEqual(str(log_entry), f"{self.user.username} - create - {log_entry.timestamp}")
