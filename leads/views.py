from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead
from .forms import LeadForm
from django.shortcuts import render, get_object_or_404, redirect  
from django.contrib.auth.decorators import login_required



@login_required
def lead_list_view(request):
    leads = Lead.objects.all()
    return render(request, 'lead_list.html', {'leads': leads})


@login_required
def lead_detail_view(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'lead_detail.html', {'lead': lead})


@login_required
def lead_edit_view(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('lead_detail', pk=lead.pk)
    else:
        form = LeadForm(instance=lead)
    return render(request, 'lead_edit.html', {'form': form, 'lead': lead})

class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    template_name = 'lead_list.html'
    context_object_name = 'leads'
    login_url = '/login/'  # Redirect to login if not authenticated

class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead
    template_name = 'lead_detail.html'
    context_object_name = 'lead'
    login_url = '/login/'  # Redirect to login if not authenticated

class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'lead_edit.html'
    success_url = reverse_lazy('lead_list')
    login_url = '/login/'  # Redirect to login if not authenticated

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = 'lead_edit.html'
    success_url = reverse_lazy('lead_list')
    login_url = '/login/'  # Redirect to login if not authenticated

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    model = Lead
    template_name = 'lead_confirm_delete.html'
    success_url = reverse_lazy('lead_list')
    login_url = '/login/'  # Redirect to login if not authenticated
