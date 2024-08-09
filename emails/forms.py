# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\emails\forms.py

from django import forms
from .models import EmailTemplate, EmailIntegration

class EmailTemplateForm(forms.ModelForm):
    class Meta:
        model = EmailTemplate
        fields = ['name', 'subject', 'body']

class EmailIntegrationForm(forms.ModelForm):
    class Meta:
        model = EmailIntegration
        fields = ['integration_name', 'status', 'settings']
