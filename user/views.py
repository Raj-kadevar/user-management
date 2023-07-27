from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import CreateView

from user.form import Reg
from user.models import User


# Create your views here.

class BookView(CreateView):

    def get(self, request, *args, **kwargs):
        form = Reg()
        return render(request,"user/form.html",{"form":form})

    def post(self, request, *args, **kwargs):
        entry = Reg(request.POST)
        if entry.is_valid():
           user_save = entry.save()
           # user_save.set_password(user_save.password)
           user_save.save()
        else:
            form = Reg()
            error = entry.errors
            return render(request, "user/form.html", {"err": error,"form":form})
        return HttpResponseRedirect("index")

def show(request):
    data = User.objects.all()
    return render(request, 'user/index.html', {"obj":data})
def delete(request, id):
    data = User.objects.get(id=id)
    data.delete()
    return redirect("index")

def update(request, id):
    get_user = User.objects.get(id=id)
    return render(request,"user/update.html",{"key":get_user})

def updater(request, id):
    name = request.POST['name']
    email = request.POST['email']
    phone_num = request.POST['phone_number']
    adrs = request.POST['address']
    get_user = User.objects.get(id=id)
    get_user.username = name
    get_user.email = email
    get_user.phone_number = phone_num
    get_user.address = adrs
    get_user.save()
    return redirect("index")