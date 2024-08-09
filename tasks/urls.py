# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\tasks\urls.py
from django.urls import path
from .views import (
    task_list_view,
    task_management_view,
    task_detail_view,
    task_edit_view,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
)

urlpatterns = [
    path('', task_list_view, name='task_list'),  # Root URL untuk daftar tugas
    path('task_management/', task_management_view, name='task_management'),  # URL untuk manajemen tugas
    path('<int:pk>/', task_detail_view, name='task_detail'),
    path('<int:pk>/edit/', task_edit_view, name='task_edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
]
