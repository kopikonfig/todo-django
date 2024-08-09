# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\reports\admin.py

from django.contrib import admin
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'generated_by')
    search_fields = ('title', 'description', 'generated_by__username')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Report, ReportAdmin)
