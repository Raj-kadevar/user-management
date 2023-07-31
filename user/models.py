from django.contrib.auth.models import AbstractUser
from django.db import models


class UserEmployee(AbstractUser):
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=80)
