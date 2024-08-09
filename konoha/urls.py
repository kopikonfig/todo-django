# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\konoha\urls.py

from django.contrib import admin
from django.urls import path, include
from . import views   
from django.contrib.auth.views import LoginView, LogoutView
from users import views as user_views  
from leads import views as lead_views
from deals import views as deal_views
from tasks import views as task_views
from emails import views as email_views
from django.views.generic import TemplateView 
from notifications import views as notification_views
from .views import logout_view  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/', include('api.urls')),
    path('customers/', include('customers.urls')),
    path('deals/', include('deals.urls')),
    path('emails/', include('emails.urls')),
    path('leads/', include('leads.urls')),
    path('logs/', include('logs.urls')),
    path('notifications/', include('notifications.urls')),
    path('reports/', include('reports.urls')),
    path('tasks/', include('tasks.urls')),
    path('users/', include('users.urls')),
    path('logout/', logout_view, name='logout'),
    path('tasks/', task_views.task_list_view, name='task_list'),
    path('dashboard/', deal_views.dashboard_view, name='dashboard'), 
    path('login/', views.LoginView.as_view(), name='login'),  
    path('help/', TemplateView.as_view(template_name='help.html'), name='help'),
    path('privacy/', TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    path('terms/', TemplateView.as_view(template_name='terms.html'), name='terms'), 
    path('deals/', include('deals.urls')), 
    path('sales-report/', user_views.sales_report_view, name='sales_report'),
    path('settings/', user_views.settings_view, name='settings'),
    path('user-management/', user_views.user_management_view, name='user_management'),
    path('notification-management/', user_views.notification_management_view, name='notification_management'),  # Mengarah ke view dashboard
    path('deal-pipeline/', deal_views.deal_pipeline_view, name='deal_pipeline'),
    path('deals/', deal_views.deal_list_view, name='deal_list'),
    path('profile/', views.profile_view, name='profile'),
    path('emails/', email_views.email_template_list_view, name='email_template_list'),

 
    path('users/', include('users.urls')), 
    path('notifications/', notification_views.NotificationListView.as_view(), name='notification_list'),
   


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
