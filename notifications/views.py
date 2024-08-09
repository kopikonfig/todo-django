# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\notifications\views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Notification
from .forms import NotificationForm
from .models import Notification


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notification_list.html'
    context_object_name = 'notifications'
    login_url = '/login/'  # Redirect to login if not authenticated

class NotificationDetailView(LoginRequiredMixin, DetailView):
    model = Notification
    template_name = 'notification_detail.html'
    context_object_name = 'notification'
    login_url = '/login/'  # Redirect to login if not authenticated

class NotificationCreateView(LoginRequiredMixin, CreateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification_form.html'
    success_url = reverse_lazy('notification_list')
    login_url = '/login/'  # Redirect to login if not authenticated

class NotificationUpdateView(LoginRequiredMixin, UpdateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification_form.html'
    success_url = reverse_lazy('notification_list')
    login_url = '/login/'  # Redirect to login if not authenticated

class NotificationDeleteView(LoginRequiredMixin, DeleteView):
    model = Notification
    template_name = 'notification_confirm_delete.html'
    success_url = reverse_lazy('notification_list')
    login_url = '/login/'  # Redirect to login if not authenticated
