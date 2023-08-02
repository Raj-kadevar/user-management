from django.contrib.auth import authenticate
from django.shortcuts import render


def login(request):
    return render(request,"book/login.html")

def index(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        print("success")
        return render(request,"book/index.html")
    else:
        error = "Username or password incorrect"
        return render(request, "book/login.html",{"errors":error})