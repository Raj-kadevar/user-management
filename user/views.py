from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from user.forms import RegistrationForm, UpdateForm
from user.models import UserEmployee


class UserView(CreateView):

    model = UserEmployee
    form_class = RegistrationForm
    template_name = 'user/form.html'

    def post(self, request, *args, **kwargs):
        user = RegistrationForm(request.POST)
        if user.is_valid():
            user_data = user.save()
            user_data.set_password(user_data.password)
            user_data.save()
        else:
            error = user.errors
            return render(request, "user/form.html", {"errors": error, "form": user})
        return HttpResponseRedirect("index")


def index(request):
    data = UserEmployee.objects.all()
    return render(request, "user/index.html", {"users": data})


def delete(request, id):
    data = UserEmployee.objects.get(id=id)
    data.delete()
    return redirect("index")


def update(request, id):
    try:
        get_user = UserEmployee.objects.get(id=id)
    except ObjectDoesNotExist as e:
        return redirect("index")

    if request.method == "POST":
        user = UpdateForm(request.POST, instance=get_user)
        if user.is_valid():
            user.save()
            return redirect("index")
    return render(request, "user/update.html", {"user_information": get_user})
