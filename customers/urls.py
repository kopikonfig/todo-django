# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\customers\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customer_list'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('create/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('<int:pk>/update/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer_delete'),
]
