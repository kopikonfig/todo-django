# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\deals\admin.py

from django.contrib import admin
from .models import Deal

class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'status', 'amount', 'close_date')
    search_fields = ('title', 'customer__name')
    list_filter = ('status', 'close_date')

admin.site.register(Deal, DealAdmin)
