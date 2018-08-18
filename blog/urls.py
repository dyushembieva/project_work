from django.urls import path
from .views import UserCreationView, IndexView, CabinetView, secret_page


app_name = 'blog'

urlpatterns = [
    path('register/', UserCreationView.as_view(), name='register'),
    path('cabinet/', CabinetView.as_view(), name='cabinet'),
    path('secret-page/', secret_page, name='secret_page'),
    path('', IndexView.as_view(), name='index'),
]
