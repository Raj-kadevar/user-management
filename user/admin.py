from django.contrib import admin
from .models import UserEmployee


@admin.register(UserEmployee)
class Users(admin.ModelAdmin):
    list_display = ("id", "username", "password", "email", "phone_number", "address")
