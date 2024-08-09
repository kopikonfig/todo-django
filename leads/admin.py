# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\leads\admin.py

from django.contrib import admin
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'source', 'created_at', 'assigned_to')
    search_fields = ('name', 'source')
    list_filter = ('status', 'source', 'assigned_to')

admin.site.register(Lead, LeadAdmin)
