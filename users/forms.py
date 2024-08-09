from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'phone_number', 'profile_picture', 'is_active']

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Current Password", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput)