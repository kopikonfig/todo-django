# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\emails\admin.py

from django.contrib import admin
from .models import EmailTemplate, EmailIntegration

class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created_at')
    search_fields = ('name', 'subject')

class EmailIntegrationAdmin(admin.ModelAdmin):
    list_display = ('integration_name', 'status')
    search_fields = ('integration_name',)

admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(EmailIntegration, EmailIntegrationAdmin)
