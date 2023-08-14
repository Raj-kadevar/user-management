from django.urls import path
from .views import DetailBook, LoginView, DeleteBook, UpdateBook, CreateBook, ManageAuthor
from book import views
from user import views as user
urlpatterns = [
    path('',LoginView.as_view(), name="login"),
    path('logout/',views.on_logout,name="logout"),
    path('index/',DetailBook.as_view(),name="index"),
    path('manage_author/<int:pk>',ManageAuthor.as_view(),name="manage_author"),
    path("deletebook/<int:book_id>/",DeleteBook.as_view(),name="deletebook"),
    path("updatebook/<int:pk>/",UpdateBook.as_view(),name="updatebook"),
    path('add_book/',CreateBook.as_view(),name="add-book"),
    path('registration_form/',user.UserView.as_view(),name="add-user"),
]