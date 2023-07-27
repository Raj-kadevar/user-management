from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class Users(admin.ModelAdmin):
    list_display = ("id", "name", "password", "email", "phone_number", "address")