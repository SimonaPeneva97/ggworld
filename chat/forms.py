from django import forms
from chat.models import Chat


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['username', 'message']

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 2:
            raise forms.ValidationError('Message must be at least 2 characters')
        return message
