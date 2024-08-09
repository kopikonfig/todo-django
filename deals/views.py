# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\deals\views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Deal
from .forms import DealForm 
from django.utils.timezone import now
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from leads.models import Lead
from customers.models import Customer
from tasks.models import Task 

# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\deals\views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from deals.models import Deal
from leads.models import Lead
from customers.models import Customer
from tasks.models import Task

@login_required
def dashboard_view(request):
    user = request.user
    
    # Mengambil data yang diperlukan untuk dashboard
    total_deals = Deal.objects.count()
    total_leads = Lead.objects.count()
    pending_tasks = Task.objects.filter(status='Pending').count()
    
    # Mengambil data aktivitas terbaru
    recent_deal = Deal.objects.order_by('-created_at').first()
    recent_task = Task.objects.filter(status='Completed').order_by('-created_at').first()
    recent_customer = Customer.objects.order_by('-updated_at').first()
    
    # Filter tasks untuk pengguna saat ini
    completed_tasks = Task.objects.filter(assigned_to=user, status='Completed').order_by('-updated_at')[:5]
    in_progress_tasks = Task.objects.filter(assigned_to=user, status='In Progress').order_by('-updated_at')[:5]
    
    # Filter aktivitas terbaru untuk pengguna saat ini
    recent_activity = []
    if recent_deal and recent_deal.assigned_to == user:
        recent_activity.append({
            'type': 'deal',
            'message': f'{user.username} added a new deal: {recent_deal.title}.',
            'time': recent_deal.created_at
        })
    if recent_task and recent_task.assigned_to == user:
        recent_activity.append({
            'type': 'task',
            'message': f'{user.username} completed task: {recent_task.title}.',
            'time': recent_task.created_at
        })
    if recent_customer and recent_customer.updated_by == user:
        recent_activity.append({
            'type': 'customer',
            'message': f'{user.username} updated customer profile: {recent_customer.name}.',
            'time': recent_customer.updated_at
        })
    
    context = {
        'total_deals': total_deals,
        'total_leads': total_leads,
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
        'in_progress_tasks': in_progress_tasks,
        'recent_activity': recent_activity,
    }
    
    return render(request, 'dashboard.html', context)


@login_required
def deal_pipeline_view(request):
    # Implementasi view untuk deal pipeline
    return render(request, 'deal_pipeline.html')

@login_required
def deal_list_view(request):
    deals = Deal.objects.all()
    return render(request, 'deal_list.html', {'deals': deals})

class DealListView(LoginRequiredMixin, ListView):
    model = Deal
    template_name = 'deal_list.html'
    context_object_name = 'deals'

class DealDetailView(LoginRequiredMixin, DetailView):
    model = Deal
    template_name = 'deal_detail.html'
    context_object_name = 'deal'

class DealCreateView(LoginRequiredMixin, CreateView):
    model = Deal
    form_class = DealForm
    template_name = 'deal_edit.html'
    success_url = reverse_lazy('deal_list')

class DealUpdateView(LoginRequiredMixin, UpdateView):
    model = Deal
    form_class = DealForm
    template_name = 'deal_edit.html'
    success_url = reverse_lazy('deal_list')

class DealDeleteView(LoginRequiredMixin, DeleteView):
    model = Deal
    template_name = 'deal_confirm_delete.html'
    success_url = reverse_lazy('deal_list')

class DealPipelineView(LoginRequiredMixin, ListView):
    model = Deal
    template_name = 'deal_pipeline.html'
    context_object_name = 'deals'

    def get_queryset(self):
        """
        Return a queryset of deals grouped by their status.
        This example assumes that the Deal model has a field 'status' which indicates the deal's current phase in the pipeline.
        """
        # Replace the following line with appropriate logic if you need more specific grouping or filtering.
        return Deal.objects.all().order_by('status')  # Order deals by status or add more complex logic if needed.

