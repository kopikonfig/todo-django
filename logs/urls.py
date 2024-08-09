# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\logs\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.LogEntryListView.as_view(), name='log_entry_list'),
    path('<int:pk>/', views.LogEntryDetailView.as_view(), name='log_entry_detail'),
]
