from django.urls import path

from exam_prep_GamesPlay.game.views import create_game, details_game, delete_game, edit_game

urlpatterns = [
    path('create/', create_game, name='create game'),
    path('edit/<id>/', edit_game, name='edit game'),
    path('details/<id>/', details_game, name='details game'),
    path('delete/<id>/', delete_game, name='delete game'),
]