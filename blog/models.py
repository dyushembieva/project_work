from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, verbose_name='Full name')

    def __str__(self):
        return self.username



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    fruit = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
