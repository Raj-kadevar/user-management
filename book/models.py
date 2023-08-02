from django.db import models
from user.models import UserEmployee
class Book(models.Model):
    name = models.CharField(max_length=50,null=False)
    price = models.DecimalField(max_length=10,decimal_places=2)
    creator = models.ManyToManyField(UserEmployee)
    author = models.CharField(max_length=20)