# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\api\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('some-model/', views.SomeModelListView.as_view(), name='some_model_list'),
    path('some-model/<int:pk>/', views.SomeModelDetailView.as_view(), name='some_model_detail'),
]
