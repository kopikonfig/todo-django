# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\tasks\tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="password")
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            due_date="2024-12-31T23:59:59Z",
            status="Pending",
            assigned_to=self.user
        )

    def test_task_str(self):
        self.assertEqual(str(self.task), self.task.title)
