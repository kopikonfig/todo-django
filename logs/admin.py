# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\logs\admin.py

from django.contrib import admin
from .models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_time', 'content_type', 'object_id', 'action_flag', 'change_message')
    list_filter = ('action_flag', 'action_time', 'user')

admin.site.register(LogEntry, LogEntryAdmin)
