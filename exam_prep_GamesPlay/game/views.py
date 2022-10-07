from django.shortcuts import render

from exam_prep_GamesPlay.common.views import get_profile
from exam_prep_GamesPlay.game.models import Game


# Create your views here.


def create_game(request):
    return render(request, 'game/create-game.html')


def details_game(request, id):
    context = {
        'game': Game.objects.get(id=id),
        'profile': get_profile()
    }
    return render(request, 'game/details-game.html', context)


def edit_game(request, id):
    context = {
        'game': Game.objects.get(id=id),
        'profile': get_profile()
    }
    return render(request, 'game/edit-game.html', context)


def delete_game(request, id):
    context = {
        'game': Game.objects.get(id=id),
        'profile': get_profile()
    }
    return render(request, 'game/delete-game.html', context)