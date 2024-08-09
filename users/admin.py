# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\users\admin.py

from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone_number', 'is_active')
    search_fields = ('user__username', 'full_name')
    list_filter = ('is_active',)

admin.site.register(UserProfile, UserProfileAdmin)
