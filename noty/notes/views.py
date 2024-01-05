from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .forms import NoteForm
from .models import Note
from user_auth.models import UserInfo

# Create your views here.
@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save(user = request.user)
            user_info, _ = UserInfo.objects.get_or_create(user = request.user)
            user_info.notes += 1
            user_info.save()
            return redirect('my-notes')

    context = {'form' : NoteForm()}
    return render(request, 'notes/create.html', context)

@login_required
@require_http_methods(['DELETE'])
def delete_note(request, note_id):
    note = get_object_or_404(Note, id = note_id)

    if request.user != note.user:
        context = {'message' : 'You do not have permission to delete this!'}
        return render(request, 'global/error.html', context)

    note.delete()
    user_info = UserInfo.objects.get(user = request.user)
    user_info.notes -= 1
    user_info.save()
    return JsonResponse({'message' : 'Deleted correctly!'}, status = 200)