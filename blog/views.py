from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, DetailView
from django.views.generic.detail import TemplateResponseMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import UserCreationModelForm,FruitModelForm
from .models import User, Category, Fruit

class UserCreationView(CreateView):
    form_class = UserCreationModelForm
    success_url = reverse_lazy('login')
    template_name = 'users/user_form.html'

class FruitViews(CreateView):
    form_class= FruitModelForm
    success_url = reverse_lazy('blog:fruit')
    template_name = 'category/fruit.html'

    def get(self, request, *args, **kwargs):
        form = FruitModelForm
        posts = Fruit.objects.all()
        print(posts)
        return render(request, self.template_name, {'category': posts})

class IndexView(TemplateView):
    template_name = 'users/index.html'



@login_required
def secret_page(request):
    return render(request, 'users/secret_page.html')


class CabinetView(LoginRequiredMixin, DetailView):
    def get_object(self):
        return self.request.user

class SingleObjectTemplateResponseMixin(TemplateResponseMixin):
    template_name_field = None
    template_name_suffix = '_detail'


