from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from .forms import UserCreationModelForm
from .models import User


class UserCreationView(CreateView):
    form_class = UserCreationModelForm
    success_url = reverse_lazy('login')
    template_name = 'users/user_form.html'


class IndexView(TemplateView):
    template_name = 'users/index.html'


@login_required
def secret_page(request):
    return render(request, 'users/secret_page.html')


class CabinetView(LoginRequiredMixin, DetailView):
    def get_object(self):
        return self.request.user