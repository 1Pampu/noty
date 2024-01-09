from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notes.models import Note
from stars.models import Star
from follows.models import Follow
from .utils import paginate_items

# Create your views here.
def home(request):
    results = Note.objects.filter(private = 0).order_by('-date')

    paginator, page = paginate_items(request, results)

    notes = []
    if request.user.is_authenticated:
        for note in page.object_list:
            stared = Star.objects.filter(user = request.user, note = note).exists()
            notes.append({'note' : note, 'star' : stared})
    else:
        for note in page.object_list:
            notes.append({'note' : note, 'star' : False})

    context = {'home_active' : True, 'notes' : notes, 'paginator': paginator, 'page': page}

    return render(request, 'feed/main.html', context)

@login_required
def my_notes(request):
    results = Note.objects.filter(user = request.user).order_by('-date')

    paginator, page = paginate_items(request, results)

    notes = []
    for note in page.object_list:
        stared = Star.objects.filter(user = request.user, note = note).exists()
        notes.append({'note' : note, 'star' : stared})

    context = {'my_notes_active' : True, 'notes' : notes, 'paginator': paginator, 'page': page}

    return render(request, 'feed/main.html', context)

@login_required
def following(request):
    following = Follow.objects.filter(follower = request.user).values_list('followed', flat=True)
    results = Note.objects.filter(user__in = following, private = 0)

    paginator, page = paginate_items(request, results)

    notes = []
    for note in page.object_list:
        stared = Star.objects.filter(user = request.user, note = note).exists()
        notes.append({'note' : note, 'star' : stared})

    context = {'following_active' : True, 'notes' : notes, 'paginator': paginator, 'page': page}

    return render(request, 'feed/main.html', context)