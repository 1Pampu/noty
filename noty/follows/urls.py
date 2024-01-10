from django.urls import path
from .views import profile, profile_stars, user_search

urlpatterns = [
    path('<str:user>', profile, name='profile'),
    path('<str:user>/stars/', profile_stars, name='profile-stars'),
    path('search/', user_search, name='user-search')
]
