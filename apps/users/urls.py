from django.urls import path
from .views import UserCreationView, IndexView, CabinetView, secret_page


app_name = 'users'

urlpatterns = [
    path('accounts/register/', UserCreationView.as_view(), name='register'),
    path('accounts/cabinet/', CabinetView.as_view(), name='cabinet'),
    path('secret-page/', secret_page, name='secret_page'),
    path('', IndexView.as_view(), name='index'),
]
