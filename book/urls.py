from django.urls import path
from book.views import MyLoginView
from user import views
urlpatterns = [
    path('',MyLoginView.as_view(),name="login"),
    path('index/',views.UserView.as_view(),name="index"),
    path('registration_form/',views.UserView.as_view(),name="add-user"),
]