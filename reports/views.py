# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\reports\views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Report
from .forms import ReportForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def report_list_view(request):
    # Pastikan nama template di sini sesuai dengan file template Anda
    return render(request, 'reports/report_list.html', {})

class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'report_list.html'
    context_object_name = 'reports'
    login_url = '/login/'  # Redirect to login if not authenticated

class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = 'report_detail.html'
    context_object_name = 'report'
    login_url = '/login/'  # Redirect to login if not authenticated

class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'report_form.html'
    success_url = reverse_lazy('report_list')
    login_url = '/login/'  # Redirect to login if not authenticated

class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'report_form.html'
    success_url = reverse_lazy('report_list')
    login_url = '/login/'  # Redirect to login if not authenticated

class ReportDeleteView(LoginRequiredMixin, DeleteView):
    model = Report
    template_name = 'report_confirm_delete.html'
    success_url = reverse_lazy('report_list')
    login_url = '/login/'  # Redirect to login if not authenticated
