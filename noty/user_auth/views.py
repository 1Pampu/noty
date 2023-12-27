from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def exit(request):
    logout(request)
    return redirect('home')