from django.shortcuts import render, redirect
from django.urls import reverse
from allauth.account.views import SignupView, LoginView, PasswordResetView

from django.contrib.auth import logout as auth_logout
from django.conf import settings

from .forms import ProfileForm
from .models import Profile

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)


# Create your views here.


class MySignupView(SignupView):
    template_name = 'signup.html'


class MyLoginView(LoginView):
    template_name = 'login.html'


def Logout(request):
    auth_logout(request)
    return redirect(reverse(settings.LOGOUT_REDIRECT_URL))


class MyPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'


def profile_detail(request):
    return render(request, 'profile_detail.html')

def profile_update(request):
    form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=request.user.profile,
    )
    if request.method == 'POST' and form.is_valid():
        profile = form.save()
        return redirect(reverse('accounts:profile_detail'))
    ctx = {
        'form': form,
    }
    return render(request, 'accounts/profile_create.html', ctx)