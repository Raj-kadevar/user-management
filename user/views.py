from django.http import HttpResponseRedirect
from django.shortcuts import render
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