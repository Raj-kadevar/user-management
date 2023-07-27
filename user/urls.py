from django.contrib import admin
from django.urls import path

from user import views

urlpatterns = [
    path('', views.BookView.as_view(), name="form"),
    path('index/', views.show,name="index"),
]