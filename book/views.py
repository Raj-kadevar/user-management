from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "book/login.html")
    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("index")
        else:
            error = "Username or password incorrect"
            return render(request, "book/login.html", {"errors": error})

def index(request):
    if request.user.is_authenticated :
        return render(request, "book/index.html")
    else:
        return redirect("login")

def on_logout(request):
    logout(request)
    return redirect("login")
