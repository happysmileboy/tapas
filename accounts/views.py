from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from allauth.account.views import SignupView, LoginView, PasswordResetView

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from django.core.mail import send_mail

from .forms import SignupForm
from .models import EmailConfirm

from .utils import generate_random_string

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


def send_confirm_mail(user):
    try:
        email_confirm = EmailConfirm.objects.get(user=user)
    except EmailConfirm.DoesNotExist:
        email_confirm = EmailConfirm.objects.create(
            user=user,
            key=generate_random_string(length=60),
        )

    url = '{0}{1}?key={2}'.format(
        'http://localhost:8000',
        reverse('accounts:confirm_email'),
        email_confirm.key,
    )
    html = '<p>계속하시려면 아래 링크를 눌러주세요.</p><a href="{0}">인증하기</a>'.format(url)
    send_mail(
        '인증 메일입니다.',
        '',
        settings.EMAIL_HOST_USER,
        [user.email],
        html_message=html,
    )


def login_and_redirect_next(request, user):
    if EmailConfirm.objects.filter(user=user, is_confirmed=True).exists():
        auth_login(request, user)
        next_url = request.GET.get('next') or settings.LOGIN_REDIRECT_URL
        return redirect(next_url)
    else:
        send_confirm_mail(user)
        return redirect(reverse('accounts:email_confirm_sent'))

def email_confirm_sent(request):
    return render(request, 'email_confirm_sent.html')


def confirm_email(request):
    key = request.GET.get('key')
    email_confirm = get_object_or_404(EmailConfirm, key=key, is_confirmed=False)
    email_confirm.is_confirmed = True
    email_confirm.save()
    return login_and_redirect_next(request, email_confirm.user)

def profile_detail(request):
    return render(request, 'profile_detail.html')