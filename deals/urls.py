from django.urls import path
from .views import DealListView, DealDetailView, DealCreateView, DealUpdateView, DealDeleteView, DealPipelineView

urlpatterns = [
    path('', DealListView.as_view(), name='deal_list'),
    path('<int:pk>/', DealDetailView.as_view(), name='deal_detail'),
    path('create/', DealCreateView.as_view(), name='deal_create'),
    path('<int:pk>/edit/', DealUpdateView.as_view(), name='deal_update'),
    path('<int:pk>/delete/', DealDeleteView.as_view(), name='deal_delete'),
    path('pipeline/', DealPipelineView.as_view(), name='deal_pipeline'),
]
