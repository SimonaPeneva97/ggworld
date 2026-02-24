from django.shortcuts import render
from .models import Chat
from .forms import ChatForm

def chat_view(request):
    messages = Chat.objects.order_by('-created_at')

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ChatForm()

    return render(request, 'chat.html', {
        'messages': messages,
        'form': form
    })


