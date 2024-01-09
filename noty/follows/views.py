from django.shortcuts import render, get_object_or_404
from notes.models import Note
from django.contrib.auth.models import User
from stars.models import Star
from .utils import follow_button, get_user_data
from feed.utils import paginate_items

# Create your views here.
def profile(request, user):
    user = get_object_or_404(User, username = user)
    follow_button(request, user)

    results = Note.objects.filter(private = 0, user = user).order_by('-date')

    paginator, page = paginate_items(request, results)

    notes = []
    if request.user.is_authenticated:
        for note in page.object_list:
            stared = Star.objects.filter(user = request.user, note = note).exists()
            notes.append({'note' : note, 'star' : stared})
    else:
        for note in page.object_list:
            notes.append({'note' : note, 'star' : False})

    user_data = get_user_data(request, user)

    context = {'notes' : notes, 'user_visiting' : user_data, 'profile' : True, 'profile_note_active' : True, 'paginator': paginator, 'page': page}

    return render(request, 'feed/main.html', context)

def profile_stars(request, user):
    user = get_object_or_404(User, username = user)
    follow_button(request, user)

    notes_stared = Star.objects.filter(user = user).values_list('note', flat = True)
    results = Note.objects.filter(private = 0, id__in=notes_stared).order_by('-date')

    paginator, page = paginate_items(request, results)

    notes = []
    if request.user.is_authenticated:
        for note in page.object_list:
            stared = Star.objects.filter(user = request.user, note = note).exists()
            notes.append({'note' : note, 'star' : stared})
    else:
        for note in page.object_list:
            notes.append({'note' : note, 'star' : False})

    user_data = get_user_data(request, user)
    context = {'notes' : notes, 'user_visiting' : user_data, 'profile' : True, 'profile_stars_active' : True, 'paginator': paginator, 'page': page}
    return render(request, 'feed/main.html', context)