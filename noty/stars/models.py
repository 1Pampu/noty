from django.db import models
from django.contrib.auth.models import User
from notes.models import Note

# Create your models here.
class Star(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'note']