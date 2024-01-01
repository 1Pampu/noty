from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notes.models import Note
from stars.models import Star

# Create your views here.
def home(request):
    results = Note.objects.filter(private = 0).order_by('-date')
    notes = []
    for note in results:
        stared = Star.objects.filter(user = request.user, note = note).exists()
        notes.append({'note' : note, 'star' : stared})
    context = {'home_active' : True, 'notes' : notes}

    return render(request, 'feed/main.html', context)

@login_required
def my_notes(request):
    results = Note.objects.filter(user = request.user).order_by('-date')
    notes = []
    for note in results:
        stared = Star.objects.filter(user = request.user, note = note).exists()
        notes.append({'note' : note, 'star' : stared})
    context = {'my_notes_active' : True, 'notes' : notes}

    return render(request, 'feed/main.html', context)

@login_required
def following(request):
    context = {'following_active' : True}
    # notes = []
    # for note in results:
    #     stared = Star.objects.filter(user = request.user, note = note).exists()
    #     notes.append({'note' : note, 'star' : stared})
    # context = {'home_active' : True, 'notes' : notes}
    return render(request, 'feed/main.html', context)