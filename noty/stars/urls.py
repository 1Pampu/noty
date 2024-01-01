from django.urls import path
from .views import handle_stars

urlpatterns = [
    path('<int:note_id>', handle_stars, name='stars'),
]