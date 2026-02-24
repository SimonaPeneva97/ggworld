from django.urls import path
from . import views
from games.views import add_game

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games_list, name='games_list'),
    path('games/<int:pk>/', views.game_details, name='game_details'),
    path('games/add/', views.add_game, name='add_game')
]
