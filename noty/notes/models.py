from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    content = models.TextField(max_length = 325, null = False)

    class Color(models.IntegerChoices):
        AMARILLO = 1, 'AMARILLO'
        VERDE = 2, 'VERDE'

    color = models.IntegerField(choices = Color.choices, default = Color.AMARILLO)
    date = models.DateTimeField(auto_now_add = True)
    private = models.BooleanField(null = False)
    stars = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} #{self.id}'