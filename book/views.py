from dataclasses import _is_dataclass_instance

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, ListView, View
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

class DetailBook(LoginRequiredMixin,ListView):
    model = Book
    template_name = "book/index.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        books = Book.objects.all()
        book_authors = BookCreation()
        return {"books": books,"book_authors":book_authors}

def on_logout(request):
    logout(request)
    return redirect("login")



class CreateBook(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        form = BookCreation()
        return render(request, "book/book_form.html",{"book":form})

    def post(self, request, *args, **kwargs):
        book = BookCreation(request.POST)
        if book.is_valid():
            book.save()
            return redirect("index")
        else:
            errors = book.errors
            return render(request, "book/book_form.html", {"form": book, "errors":errors})


class DeleteBook(LoginRequiredMixin,DeleteView):
    def get(self, request, *args, **kwargs):
        book = Book.objects.get(id=kwargs.get("book_id"))
        book.delete()
        return redirect("index")


class UpdateBook(LoginRequiredMixin,UpdateView):
    form_class = BookCreation
    template_name = "book/update.html"
    success_url = reverse_lazy("index")
    queryset = Book.objects.all()


class AddAuthor(UpdateView):

    form_class = BookCreation
    template_name = "book/index.html"
    success_url = reverse_lazy("index")
    queryset = Book.objects.all()

    def post(self, request, *args, **kwargs):
        breakpoint()
        authors = Book.objects.get(id=kwargs.get("pk"))
        author_list = self.request.POST.getlist('authors[]')
        object = Book.objects.filter(id__in=[int(i) for i in author_list])
        authors.author = object
        authors.save()
        return JsonResponse({"status":"success"})

