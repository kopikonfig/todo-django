# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\logs\models.py

from django.db import models
from django.contrib.auth.models import User

class LogEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs_logentry_set')
    action_time = models.DateTimeField(auto_now_add=True)
    content_type = models.CharField(max_length=255)
    object_id = models.PositiveIntegerField()
    action_flag = models.PositiveIntegerField()
    change_message = models.TextField()

    def __str__(self):
        return f'{self.user} - {self.action_time}'
