# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\reports\models.py

from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    generated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
