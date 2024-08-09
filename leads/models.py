# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\leads\models.py

from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('unqualified', 'Unqualified'),
    ]
    SOURCE_CHOICES = [
        ('web', 'Web'),
        ('phone', 'Phone'),
        ('referral', 'Referral'),
        ('event', 'Event'),
    ]

    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='web')
    contact_information = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
