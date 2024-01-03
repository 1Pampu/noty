from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Follow(models.Model):
    follower = models.ForeignKey(User, related_name = 'following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name = 'followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['follower', 'followed']

    def clean(self):
        if self.follower == self.followed:
            raise ValidationError("Cannot follow yourself!")

    def save(self, *args, **kwargs):
            self.full_clean()
            super().save(*args, **kwargs)