# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\emails\views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import EmailTemplate, EmailIntegration
from .forms import EmailTemplateForm, EmailIntegrationForm


@login_required
def email_template_list_view(request):
    email_templates = EmailTemplate.objects.all()
    return render(request, 'email_template_list.html', {'email_templates': email_templates})

class EmailTemplateListView(LoginRequiredMixin, ListView):
    model = EmailTemplate
    template_name = 'email_template_list.html'
    context_object_name = 'templates'
    login_url = '/login/'  # Redirect to login page if not authenticated

class EmailTemplateDetailView(LoginRequiredMixin, DetailView):
    model = EmailTemplate
    template_name = 'email_template_detail.html'
    context_object_name = 'template'
    login_url = '/login/'  # Redirect to login page if not authenticated

class EmailTemplateCreateView(LoginRequiredMixin, CreateView):
    model = EmailTemplate
    form_class = EmailTemplateForm
    template_name = 'email_template_edit.html'
    success_url = reverse_lazy('email_template_list')
    login_url = '/login/'  # Redirect to login page if not authenticated

class EmailTemplateUpdateView(LoginRequiredMixin, UpdateView):
    model = EmailTemplate
    form_class = EmailTemplateForm
    template_name = 'email_template_edit.html'
    success_url = reverse_lazy('email_template_list')
    login_url = '/login/'  # Redirect to login page if not authenticated

class EmailTemplateDeleteView(LoginRequiredMixin, DeleteView):
    model = EmailTemplate
    template_name = 'email_template_confirm_delete.html'
    success_url = reverse_lazy('email_template_list')
    login_url = '/login/'  # Redirect to login page if not authenticated

class EmailIntegrationListView(LoginRequiredMixin, ListView):
    model = EmailIntegration
    template_name = 'email_integration_list.html'
    context_object_name = 'integrations'
    login_url = '/login/'  # Redirect to login page if not authenticated

class EmailIntegrationDetailView(LoginRequiredMixin, DetailView):
    model = EmailIntegration
    template_name = 'email_integration_detail.html'
    context_object_name = 'integration'
    login_url = '/login/'  # Redirect to login page if not authenticated

class EmailIntegrationCreateView(LoginRequiredMixin, CreateView):
    model = EmailIntegration
    form_class = EmailIntegrationForm
    template_name = 'email_integration_edit.html'
    success_url = reverse_lazy('email_integration_list')
    login_url = '/login/'  # Redirect to login page if not authenticated

class EmailIntegrationUpdateView(LoginRequiredMixin, UpdateView):
    model = EmailIntegration
    form_class = EmailIntegrationForm
    template_name = 'email_integration_edit.html'
    success_url = reverse_lazy('email_integration_list')
    login_url = '/login/'  # Redirect to login page if not authenticated
