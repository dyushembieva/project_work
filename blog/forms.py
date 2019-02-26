from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import get_user_model
from django.forms import ModelForm
from .models import Fruit

User = get_user_model()

class UserCreationModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'password1', 'password2']


class FruitModelForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'price')
