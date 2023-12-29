from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notes.models import Note

# Create your views here.
def home(request):
    context = {'home_active' : True}
    return render(request, 'feed/home.html', context)

@login_required
def my_notes(request):
    results = Note.objects.filter(user = request.user)
    context = {'my_notes_active' : True, 'notes' : results}
    return render(request, 'feed/my-notes.html', context)

@login_required
def following(request):
    context = {'following_active' : True}
    return render(request, 'feed/following.html', context)