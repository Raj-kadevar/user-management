from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages


# Create your views here.

class MyLoginView(LoginView):
    template_name = "book/login.html"
    authentication_form = AuthenticationForm
    LOGIN_REDIRECT_URL = 'index'
