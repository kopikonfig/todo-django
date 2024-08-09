# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\tasks\forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Task Title'}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Task Description'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'input', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'select'}),
            'assigned_to': forms.Select(attrs={'class': 'select'}),
        }
