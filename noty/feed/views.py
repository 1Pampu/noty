from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notes.models import Note

# Create your views here.
def home(request):
    results = Note.objects.filter(private = 0).order_by('-date')
    context = {'home_active' : True, 'notes' : results}
    return render(request, 'feed/main.html', context)

@login_required
def my_notes(request):
    results = Note.objects.filter(user = request.user).order_by('-date')
    context = {'my_notes_active' : True, 'notes' : results}
    return render(request, 'feed/main.html', context)

@login_required
def following(request):
    context = {'following_active' : True}
    return render(request, 'feed/main.html', context)