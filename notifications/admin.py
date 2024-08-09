# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\notifications\admin.py

from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'message', 'is_read', 'timestamp')
    search_fields = ('user__username', 'title', 'message')
    list_filter = ('is_read', 'timestamp')

admin.site.register(Notification, NotificationAdmin)
