from django.forms import ModelForm
from .models import Note

class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = '__all__'
        exclude = ('user','stars',)

    def save(self, commit = True, user = None):
        instance = super().save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance