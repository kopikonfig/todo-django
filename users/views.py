from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .models import UserProfile
from .forms import UserProfileForm, UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash 
from django.contrib.auth.decorators import login_required

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Update session to prevent logout
            return redirect('profile')  # Redirect to profile after successful password change
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def profile_view(request):
    userprofile, created = UserProfile.objects.get_or_create(user=request.user)
    context = {'userprofile': userprofile}
    return render(request, 'profile.html', context)

@login_required
def update_profile_view(request):
    userprofile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=userprofile)
    return render(request, 'profile_edit.html', {'form': form})

@login_required
def settings_view(request):
    return render(request, 'settings.html')

@login_required
def sales_report_view(request):
    return render(request, 'sales_report.html')

@login_required
def user_management_view(request):
    return render(request, 'user_management.html')

@login_required
def notification_management_view(request):
    return render(request, 'notification_management.html')

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'userprofile'
    login_url = '/login/'

    def get_object(self, queryset=None):
        # Ensure that UserProfile exists for the logged-in user
        userprofile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return userprofile

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('profile')
    login_url = '/login/'

    def get_object(self, queryset=None):
        # Ensure that UserProfile exists for the logged-in user
        userprofile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return userprofile
