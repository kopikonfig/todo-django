# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\customers\forms.py

from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number', 'address']
