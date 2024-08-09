# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\tasks\models.py

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Added
    updated_at = models.DateTimeField(auto_now=True)      # Added

    def __str__(self):
        return self.title
