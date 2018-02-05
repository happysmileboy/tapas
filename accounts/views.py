from django.shortcuts import render, redirect
from django.urls import reverse
from allauth.account.views import SignupView, LoginView, PasswordResetView

from django.contrib.auth import logout as auth_logout
from django.conf import settings


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
