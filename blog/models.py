from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, verbose_name='Full name')

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')

    class Meta:
        verbose_name = "Категория"

    def __str__(self):
        return 'Категория %s' % self.name

class Fruit(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.IntegerField(default=0, verbose_name='Цена')
    # image = models.CharField(max_length=255, verbose_name='Ссылка на картинку')
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Фрукт"
        verbose_name_plural = "Фрукты"

    def __str__(self):
        return 'Фрукт %s' % self.name

class Vegetable(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.IntegerField(default=0, verbose_name='Цена')
    # image = models.CharField(max_length=255, verbose_name='Ссылка на картинку')
    
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Овощь"
        verbose_name_plural = "Овощи"

    def __str__(self):
        return 'Овощь %s' % self.name