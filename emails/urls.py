# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\emails\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmailTemplateListView.as_view(), name='email_template_list'),
    path('template/<int:pk>/', views.EmailTemplateDetailView.as_view(), name='email_template_detail'),
    path('template/create/', views.EmailTemplateCreateView.as_view(), name='email_template_create'),
    path('template/<int:pk>/update/', views.EmailTemplateUpdateView.as_view(), name='email_template_update'),
    path('template/<int:pk>/delete/', views.EmailTemplateDeleteView.as_view(), name='email_template_delete'),
    path('integration/', views.EmailIntegrationListView.as_view(), name='email_integration_list'),
    path('integration/<int:pk>/', views.EmailIntegrationDetailView.as_view(), name='email_integration_detail'),
    path('integration/create/', views.EmailIntegrationCreateView.as_view(), name='email_integration_create'),
    path('integration/<int:pk>/update/', views.EmailIntegrationUpdateView.as_view(), name='email_integration_update'),
]
