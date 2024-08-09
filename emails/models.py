# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\emails\models.py

from django.db import models

class EmailTemplate(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EmailIntegration(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    integration_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='inactive')
    settings = models.JSONField()  # Storing settings as JSON
    
    def __str__(self):
        return self.integration_name
