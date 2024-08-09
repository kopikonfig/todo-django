# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\deals\tests.py

from django.test import TestCase
from .models import Deal
from customers.models import Customer

class DealModelTestCase(TestCase):
    def setUp(self):
        customer = Customer.objects.create(name="John Doe", email="john@example.com")
        Deal.objects.create(title="Deal 1", customer=customer, status="new", amount=1000.00, close_date="2024-12-31")

    def test_deal_str(self):
        deal = Deal.objects.get(title="Deal 1")
        self.assertEqual(str(deal), "Deal 1")
