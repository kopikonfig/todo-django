# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\api\models.py

from django.db import models

class SomeModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
