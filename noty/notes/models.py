from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):

    class Color(models.IntegerChoices):
        AMARILLO = 1, 'AMARILLO'
        VERDE = 2, 'VERDE'

    color = models.IntegerField(choices = Color.choices, default = Color.AMARILLO)
    content = models.TextField(max_length = 1500, null = False)
    date = models.DateField(auto_now_add = True)
    public = models.BooleanField(null = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} #{self.id}'