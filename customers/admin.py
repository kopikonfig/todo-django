# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\customers\admin.py

from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email')

admin.site.register(Customer, CustomerAdmin)
