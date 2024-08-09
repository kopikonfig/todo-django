# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\customers\views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm

class CustomerListView(LoginRequiredMixin, ListView):  # Menambahkan LoginRequiredMixin
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(LoginRequiredMixin, DetailView):  # Menambahkan LoginRequiredMixin
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'

class CustomerCreateView(LoginRequiredMixin, CreateView):  # Menambahkan LoginRequiredMixin
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_edit.html'
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(LoginRequiredMixin, UpdateView):  # Menambahkan LoginRequiredMixin
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_edit.html'
    success_url = reverse_lazy('customer_list')

class CustomerDeleteView(LoginRequiredMixin, DeleteView):  # Menambahkan LoginRequiredMixin
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')
