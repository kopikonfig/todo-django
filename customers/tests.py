# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\customers\tests.py

from django.test import TestCase
from .models import Customer

class CustomerModelTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="John Doe", email="john@example.com", phone_number="1234567890")

    def test_customer_str(self):
        customer = Customer.objects.get(name="John Doe")
        self.assertEqual(str(customer), "John Doe")
