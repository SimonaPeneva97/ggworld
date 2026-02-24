from django import forms
from reviews.models import Review, Game  # не забравяй да импортираш Game

class ReviewForm(forms.ModelForm):
    # Използваме ModelChoiceField за избиране на игра
    game = forms.ModelChoiceField(
        queryset=Game.objects.all(),
        label='Select Game',
        empty_label='Choose a game',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    comment = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write your review here...', 'rows': 4}),
        label='Your Review'
    )

    class Meta:
        model = Review
        fields = ('username', 'game', 'rating', 'comment')
        labels = {
            'username': 'Your Name',
            'rating': 'Rating (1-5)',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError('Username must be at least 3 characters long.')
        return username

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise forms.ValidationError('Rating must be between 1 and 5.')
        return rating



