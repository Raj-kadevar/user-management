from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from user.forms import Registration
from user.models import UserEmployee


class UserView(CreateView):
    def get_queryset(self):
        return UserEmployee.objects.all()

    def get_context_data(self, **kwargs):
        form = Registration
        return {"form": form}

    def get_template_names(self):
        return "user/form.html"

    def post(self, request, *args, **kwargs):
        user = Registration(request.POST)
        if user.is_valid():
            user_data = user.save()
            user_data.set_password(user_data.password)
            user_data.save()
        else:
            form = Registration()
            error = user.errors
            return render(request, "user/form.html", {"err": error, "form": user})
        return HttpResponseRedirect("index")


def index(request):
    data = UserEmployee.objects.all()
    return render(request, "user/index.html", {"obj": data})


def delete(request, id):
    data = UserEmployee.objects.get(id=id)
    data.delete()
    return redirect("index")


def update(request, id):
    get_user = UserEmployee.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone_num = request.POST["phone_number"]
        address = request.POST["address"]
        get_user = UserEmployee.objects.get(id=id)
        get_user.username = name
        get_user.email = email
        get_user.phone_number = phone_num
        get_user.address = address
        get_user.save()
        return redirect("index")
    return render(request, "user/update.html", {"key": get_user})
