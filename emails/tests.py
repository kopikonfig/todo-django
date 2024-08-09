# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\emails\tests.py

from django.test import TestCase
from .models import EmailTemplate, EmailIntegration

class EmailTemplateModelTestCase(TestCase):
    def setUp(self):
        EmailTemplate.objects.create(name="Welcome Email", subject="Welcome!", body="Thank you for joining us.")

    def test_email_template_str(self):
        template = EmailTemplate.objects.get(name="Welcome Email")
        self.assertEqual(str(template), "Welcome Email")

class EmailIntegrationModelTestCase(TestCase):
    def setUp(self):
        EmailIntegration.objects.create(integration_name="Mailgun", status="active", settings={"api_key": "123456"})

    def test_email_integration_str(self):
        integration = EmailIntegration.objects.get(integration_name="Mailgun")
        self.assertEqual(str(integration), "Mailgun")
