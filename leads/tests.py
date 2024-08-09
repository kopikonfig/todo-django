# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\leads\tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Lead

class LeadModelTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser", password="password")
        Lead.objects.create(name="Test Lead", status="new", source="web", contact_information="1234567890", assigned_to=user)

    def test_lead_str(self):
        lead = Lead.objects.get(name="Test Lead")
        self.assertEqual(str(lead), "Test Lead")
