from django.urls import path
from .views import RegisterView, ProfileView, EditProfileView, update_profile_view, change_password_view


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
  path('change_password/', change_password_view, name='change_password'),
]