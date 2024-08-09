# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\api\tests.py

from django.test import TestCase
from .models import SomeModel

class SomeModelTestCase(TestCase):
    def setUp(self):
        SomeModel.objects.create(name="Test Model", description="This is a test.")

    def test_model_str(self):
        model = SomeModel.objects.get(name="Test Model")
        self.assertEqual(str(model), "Test Model")
