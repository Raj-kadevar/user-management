from django.urls import path

from user import views

urlpatterns = [
    path("", views.BookView.as_view(), name="add-user"),
    path("index/", views.show, name="index"),
    path("update/<int:id>", views.update, name="update"),
    path("updater/<int:id>", views.updater, name="updater"),
    path("delete/<int:id>", views.delete, name="delete"),
]
