from django.urls import path
from .views import create_note, delete_note

urlpatterns = [
    path('create/', create_note, name='create-note'),
    path('delete/<int:note_id>', delete_note, name='delete-note'),
]
