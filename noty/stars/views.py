from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from notes.models import Note
from .models import Star

# Create your views here.
@login_required
def handle_stars(request, note_id):
    note = get_object_or_404(Note, id = note_id)
    already_stared = Star.objects.filter(user = request.user, note = note).exists()

    if request.method == 'POST':

        if already_stared:
            return JsonResponse({'message' : 'Already stared!'}, status = 409)

        star = Star(user = request.user, note = note)
        star.save()
        note.stars += 1
        note.save()
        return JsonResponse({'message' : 'Succesfully stared!'})

    if request.method == 'DELETE':

        if not already_stared:
            return JsonResponse({'message' : 'Not stared!'}, status = 409)

        star = Star.objects.filter(user = request.user, note = note)
        star.delete()
        note.stars -= 1
        note.save()
        return JsonResponse({'message' : 'Succesfully unstared!'})

    return JsonResponse({'star' : already_stared})

