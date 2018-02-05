from django.urls import path
from allauth.account.views import SignupView, LoginView, PasswordResetView
from . import views
# Create your views here.


class MySignupView(SignupView):
    template_name = 'signup.html'

class MyLoginView(LoginView):
    template_name = 'login.html'

class MyPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'

app_name = 'accounts'


urlpatterns = [
    path('login/', MyLoginView.as_view(), name='account_login'),
    path('signup/', MySignupView.as_view(), name='account_signup'),
    path('password_reset/', MyPasswordResetView.as_view(), name='account_reset_password'),
    path('profile/', views.profile_detail, name='profile_detail')
]