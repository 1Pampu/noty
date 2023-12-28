from django.urls import path
from .views import exit, register

urlpatterns = [
    path('exit/', exit, name='exit'),
    path('register/', register, name='register'),
]
