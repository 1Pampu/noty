from django.shortcuts import render, get_object_or_404
from .models import Follow
from user_auth.models import UserInfo

def follow_button(request, user):
    if request.method == 'POST':
        if request.POST.get('_method') == 'DELETE':
            try:
                follow = get_object_or_404(Follow, follower = request.user, followed = user)
                follow.delete()
                user_followed_info = UserInfo.objects.get(user = user)
                user_followed_info.followers -= 1
                user_followed_info.save()
                user_info = UserInfo.objects.get(user = request.user)
                user_info.following -= 1
                user_info.save()
            except Exception as Error:
                context = {'message' : Error}
                return render(request, 'global/error.html', context)

        else:
            try:
                follow = Follow(follower = request.user, followed = user)
                follow.save()
                user_followed_info, _ = UserInfo.objects.get_or_create(user = user)
                user_followed_info.followers += 1
                user_followed_info.save()
                user_info, _ = UserInfo.objects.get_or_create(user = request.user)
                user_info.following += 1
                user_info.save()
            except Exception as Error:
                context = {'message' : Error}
                return render(request, 'global/error.html', context)

def get_user_data(request, user):
    user_data = {}
    user_info, _ = UserInfo.objects.get_or_create(user = user)

    user_data['username'] = user.username

    actual_following = Follow.objects.filter(follower = request.user, followed = user).exists()
    user_data['actual_following'] = actual_following

    user_data['followers'] = user_info.followers
    user_data['following'] = user_info.following
    user_data['stars'] = user_info.stars
    user_data['total_notes'] = user_info.notes

    return user_data