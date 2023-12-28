from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'home_active' : True}
    return render(request, 'feed/home.html', context)

def my_notes(request):
    context = {'my_notes_active' : True}
    return render(request, 'feed/my-notes.html', context)

def following(request):
    context = {'following_active' : True}
    return render(request, 'feed/following.html', context)