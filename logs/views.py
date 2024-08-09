# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\logs\views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import LogEntry

class LogEntryListView(LoginRequiredMixin, ListView):
    model = LogEntry
    template_name = 'log_entry_list.html'
    context_object_name = 'logs'
    login_url = '/login/'  # Redirect to login if not authenticated

class LogEntryDetailView(LoginRequiredMixin, DetailView):
    model = LogEntry
    template_name = 'log_entry_detail.html'
    context_object_name = 'log'
    login_url = '/login/'  # Redirect to login if not authenticated
