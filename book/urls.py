from django.urls import path
from book import views
from user import views as user
urlpatterns = [
    path('',views.LoginView.as_view(), name="login"),
    path('logout/',views.on_logout,name="logout"),
    path('index/',views.index,name="index"),
    path('delete/<int:id>',views.index,name="delete"),
    path('update/<int:id>',views.index,name="update"),
    path('add_book/',views.BookView.as_view(),name="add-book"),
    path('registration_form/',user.UserView.as_view(),name="add-user"),
]