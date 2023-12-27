from django.urls import path
from .views import home, my_notes

urlpatterns = [
    path('home/', home, name='home'),
    path('my-notes/', my_notes, name='my-notes'),
]
