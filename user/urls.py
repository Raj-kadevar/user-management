from django.urls import path
from user import views

urlpatterns = [
    path("", views.UserView.as_view(), name="add-user"),
    path("index/", views.index, name="index"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
]
