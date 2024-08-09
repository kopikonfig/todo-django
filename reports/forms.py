# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\reports\forms.py

from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description']
