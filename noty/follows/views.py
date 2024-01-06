from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from notes.models import Note
from django.contrib.auth.models import User
from stars.models import Star
from .utils import follow_button, get_user_data

# Create your views here.
@login_required
def profile(request, user):
    user = get_object_or_404(User, username = user)
    follow_button(request, user)

    results = Note.objects.filter(private = 0, user = user).order_by('-date')
    notes = []
    for note in results:
        stared = Star.objects.filter(user = request.user, note = note).exists()
        notes.append({'note' : note, 'star' : stared})

    user_data = get_user_data(request, user)
    context = {'notes' : notes, 'user_visiting' : user_data, 'profile' : True, 'profile_note_active' : True}
    return render(request, 'feed/main.html', context)

@login_required
def profile_stars(request, user):
    user = get_object_or_404(User, username = user)
    follow_button(request, user)

    notes_stared = Star.objects.filter(user = user).values_list('note', flat = True)
    results = Note.objects.filter(private = 0, id__in=notes_stared).order_by('-date')
    notes = []
    for note in results:
        notes.append({'note' : note, 'star' : True})

    user_data = get_user_data(request, user)
    context = {'notes' : notes, 'user_visiting' : user_data, 'profile' : True, 'profile_stars_active' : True}
    return render(request, 'feed/main.html', context)