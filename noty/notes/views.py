from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NoteForm

# Create your views here.
@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('my-notes')

    context = {'form' : NoteForm()}
    return render(request, 'notes/create.html', context)