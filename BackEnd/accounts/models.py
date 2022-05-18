from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mileage = models.IntegerField(default=0)
    # age = models.IntegerField()


class Item(models.Model):
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    price = models.IntegerField()
    photo_url = models.URLField()
    bought_users = models.ManyToManyField(User, related_name='bought_items')