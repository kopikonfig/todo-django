# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\notifications\forms.py

from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['title', 'message', 'is_read']
