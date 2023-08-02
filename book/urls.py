from django.urls import path
from book import views
from user import views as user
urlpatterns = [
    path('',views.login, name="login"),
    path('index/',views.index,name="index"),
    path('registration_form/',user.UserView.as_view(),name="add-user"),
]