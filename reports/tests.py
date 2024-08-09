# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\reports\tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Report

class ReportModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="password")
        self.report = Report.objects.create(
            title="Test Report",
            description="This is a test report",
            generated_by=self.user
        )

    def test_report_str(self):
        self.assertEqual(str(self.report), self.report.title)
