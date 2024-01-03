from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Follow
from notes.models import Note
from django.contrib.auth.models import User
from stars.models import Star
from django.db.models import Sum

# Create your views here.
@login_required
def profile(request, user):
    user = get_object_or_404(User, username = user)

    if request.method == 'POST':
        if request.POST.get('_method') == 'DELETE':
            try:
                follow = get_object_or_404(Follow, follower = request.user, followed = user)
                follow.delete()
            except Exception as Error:
                context = {'message' : Error}
                return render(request, 'global/error.html', context)
        else:
            try:
                follow = Follow(follower = request.user, followed = user)
                follow.save()
            except Exception as Error:
                context = {'message' : Error}
                return render(request, 'global/error.html', context)

    if request.method == 'DELETE':
        pass

    results = Note.objects.filter(private = 0, user = user).order_by('-date')
    notes = []
    for note in results:
        stared = Star.objects.filter(user = request.user, note = note).exists()
        notes.append({'note' : note, 'star' : stared})

    user_data = {}
    actual_following = Follow.objects.filter(follower = request.user, followed = user).exists()
    user_data['actual_following'] = actual_following

    followers = Follow.objects.filter(followed = user).count()
    user_data['followers'] = followers

    following = Follow.objects.filter(follower = user).count()
    user_data['following'] = following

    sum_stars = results.aggregate(Sum('stars'))['stars__sum']
    user_data['stars'] = sum_stars

    user_data['total_notes'] = results.count()
    user_data['username'] = user.username

    context = {'notes' : notes, 'user_visiting' : user_data, 'profile' : True}
    return render(request, 'feed/main.html', context)