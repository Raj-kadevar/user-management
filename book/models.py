from django.db import models
from user.models import UserEmployee
class Book(models.Model):
    name = models.CharField(max_length=50,null=False)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    creator = models.ForeignKey(UserEmployee,on_delete=models.PROTECT,related_name="as_creator")
    author = models.ManyToManyField(UserEmployee)