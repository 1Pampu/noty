from django.urls import path
from .views import exit

urlpatterns = [
    path('exit/', exit, name='exit'),
]
