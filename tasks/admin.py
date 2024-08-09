# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\tasks\admin.py

from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'status', 'assigned_to')
    search_fields = ('title', 'description', 'assigned_to__username')
    list_filter = ('status', 'due_date')

admin.site.register(Task, TaskAdmin)
