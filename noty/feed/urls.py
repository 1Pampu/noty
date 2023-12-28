from django.urls import path
from .views import home, my_notes, following

urlpatterns = [
    path('home/', home, name='home'),
    path('my-notes/', my_notes, name='my-notes'),
    path('following/', following, name='following'),
]
