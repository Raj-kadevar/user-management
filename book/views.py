from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import DeleteView, UpdateView, DetailView

from book.forms import BookCreation, UpdateFrom
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

class DetailBook(LoginRequiredMixin,DetailView):
    model = Book

    def get(self, request, *args, **kwargs):
         books = Book.objects.all()
         return render(request, "book/index.html", {"books": books})

def on_logout(request):
    logout(request)
    return redirect("login")



class CreateBook(LoginRequiredMixin,View):
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


class DeleteBook(LoginRequiredMixin,DeleteView):
    model = Book


    def get(self, request, *args, **kwargs):
        book = Book.objects.get(id=kwargs.get("book_id"))
        book.delete()
        return redirect("index")


class UpdateBook(LoginRequiredMixin,UpdateView):
    model = Book
    fields = ["price"]
    def get(self, request, *args, **kwargs):
        book = Book.objects.get(id=kwargs.get("id"))
        return render(request, "book/update.html", {"book": book})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            book = Book.objects.get(id=kwargs.get("id"))
            book_update = UpdateFrom(request.POST, instance=book)
            book_update.save()
            return redirect("index")
        return render(request, "book/update.html", {"book": book})

