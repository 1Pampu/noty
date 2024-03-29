from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForm
from .models import UserInfo

# Create your views here.
def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data = request.POST)

        if user_creation_form.is_valid():
            new_user = user_creation_form.save()
            UserInfo.objects.create(user = new_user)
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')

    context = {'form': CustomUserCreationForm()}
    return render(request, 'registration/register.html', context)