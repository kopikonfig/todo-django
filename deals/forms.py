# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\deals\forms.py

from django import forms
from .models import Deal

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['title', 'customer', 'status', 'amount', 'close_date', 'description']
