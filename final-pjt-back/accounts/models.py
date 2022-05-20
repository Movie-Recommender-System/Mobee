from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mileage = models.IntegerField(default=0)


class Item(models.Model):
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    price = models.IntegerField()
    photo_url = models.URLField()
    purchased_users = models.ManyToManyField(User, through='PurchaseList', related_name='inventory')


class PurchaseList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)