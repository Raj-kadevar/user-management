from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=30, null=False)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=80)
