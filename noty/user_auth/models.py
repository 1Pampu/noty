from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    notes = models.IntegerField(default=0)
    stars = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Info, Followers: {self.followers}, Stars: {self.stars}'