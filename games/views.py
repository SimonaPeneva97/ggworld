from django.shortcuts import render, get_object_or_404, redirect
from games.models import Game
from games.forms import GameForm
from reviews.forms import ReviewForm


def home(request):
    return render(request, 'index.html')


def games_list(request):
    games = Game.objects.all()
    return render(request, 'games_list.html', {'games': games})


def game_details(request, pk):
    game = get_object_or_404(Game, pk=pk)
    reviews = game.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.save()
            return redirect('game_details', pk=pk)
    else:
        form = ReviewForm()

    return render(request, 'games_details.html', {
        'game': game,
        'reviews': reviews,
        'form': form
    })



def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('games_list')
    else:
        form = GameForm()

    return render(request, 'add_game.html', {'form': form})





