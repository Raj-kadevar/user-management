from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View

from book.forms import BookCreation
from book.models import Book


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
        books = Book.objects.all()
        return render(request, "book/index.html",{"books":books})
    else:
        return redirect("login")


def on_logout(request):
    logout(request)
    return redirect("login")



class BookView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated :
            return redirect("login")

        form = BookCreation
        return render(request, "book/book_form.html",{"form":form})

    def post(self, request, *args, **kwargs):
        book = BookCreation(request.POST)
        if book.is_valid():
            book.save()
            return redirect("index")
        else:
            errors = book.errors
            return render(request, "book/book_form.html", {"form": book, "errors":errors})

def delete(request, id):
    pass

def update(request, id):
    pass
