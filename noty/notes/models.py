from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    content = models.TextField(max_length = 250, null = False)

    class Color(models.IntegerChoices):
        Yellow = 1, 'Yellow'
        Green = 2, 'Green'
        Red = 3, 'Red'
        Orange = 4, 'Orange'
        Blue = 5, 'Blue'
        Pink = 6, 'Pink'

    color = models.IntegerField(choices = Color.choices, default = Color.Yellow)
    date = models.DateTimeField(auto_now_add = True)
    private = models.BooleanField(null = False)
    stars = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} #{self.id}'