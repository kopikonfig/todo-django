from django.contrib.auth.views import LoginView as AuthLoginView
from django.shortcuts import get_object_or_404, render 
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

from users.models import UserProfile
 
@login_required
def profile_view(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profile.html', {'userprofile': userprofile})

class HelpView(TemplateView):
    template_name = 'help.html'

class PrivacyView(TemplateView):
    template_name = 'privacy.html'

class TermsView(TemplateView):
    template_name = 'terms.html'


def index(request):
    return render(request, 'index.html')

class LoginView(AuthLoginView):
    template_name = 'login.html'

    from django.contrib.auth import logout
from django.urls import reverse

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')