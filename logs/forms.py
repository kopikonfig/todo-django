# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\logs\forms.py

from django import forms
from .models import LogEntry

class LogEntryForm(forms.ModelForm):
    class Meta:
        model = LogEntry
        fields = ['user', 'action', 'description']
