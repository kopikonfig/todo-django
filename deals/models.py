# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\deals\models.py

from django.db import models
from customers.models import Customer

class Deal(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('closed_won', 'Closed Won'),
        ('closed_lost', 'Closed Lost'),
    ]
    
    title = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    close_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
