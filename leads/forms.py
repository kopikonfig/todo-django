# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\leads\forms.py

from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'status', 'source', 'contact_information', 'assigned_to', 'notes']
