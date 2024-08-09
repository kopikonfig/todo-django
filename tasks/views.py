# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\tasks\views.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django import forms
from .forms import TaskForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 

@login_required
def task_list_view(request):
    # Filter tasks to only show those assigned to the current user
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def task_management_view(request): 
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'task_management.html', {'tasks': tasks})


@login_required
def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

@login_required
def task_edit_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form, 'task': task})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    login_url = '/login/'

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
    login_url = '/login/'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'assigned_to']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.instance.created_by = user

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Task'
        context['submit_button_text'] = 'Create Task'
        return context

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Task'
        context['submit_button_text'] = 'Save Changes'
        return context

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
    login_url = '/login/'
