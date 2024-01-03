from django.urls import path
from .views import profile

urlpatterns = [
    path('<str:user>', profile, name='profile'),
]
