from django import forms
from games.models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'description', 'genre', 'price', 'image')
        labels = {
            'title': 'Game Title',
            'description': 'Description',
            'genre': 'Genre',
            'price': 'Price ($)',
            'image': 'Game Image',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter game title'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter game description'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Enter genre'}),
            'price': forms.NumberInput(attrs={'min': 0, 'step': 0.01}),
        }
