from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'feed/home.html')

def my_notes(request):
    return render(request, 'feed/my-notes.html')