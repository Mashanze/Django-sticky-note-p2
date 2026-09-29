from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'color']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note title...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your note here...', 'rows': 3}),
            'color': forms.Select(attrs={'class': 'form-select'}),
        }