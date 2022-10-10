from django.shortcuts import render, redirect

from exam_prep_GamesPlay.common.utils import get_profile
from exam_prep_GamesPlay.game.forms import CreateGame, EditGame, DeleteGame
from exam_prep_GamesPlay.game.models import Game


# Create your views here.


def create_game(request):
    form = CreateGame()
    if request.method == 'POST':
        form = CreateGame(request.POST)
        form.full_clean()
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'profile': get_profile(),
        'form': form,
    }
    return render(request, 'game/create-game.html', context)


def details_game(request, id):
    context = {
        'game': Game.objects.get(id=id),
        'profile': get_profile()
    }
    return render(request, 'game/details-game.html', context)


def edit_game(request, id):
    game = Game.objects.get(id=id)
    form = EditGame(instance=game)

    if request.method == 'POST':
        form = EditGame(request.POST, instance=game)
        form.full_clean()
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'game': game,
        'profile': get_profile(),
        'form': form,
    }
    return render(request, 'game/edit-game.html', context)


def delete_game(request, id):
    game = Game.objects.get(id=id)
    form = DeleteGame(instance=game)
    for fieldname in form.fields:
        form.fields[fieldname].disabled = True
    if request.method == 'POST':
        game.delete()
        return redirect('dashboard')

    context = {
        'game': game,
        'profile': get_profile(),
        'form': form,
    }
    return render(request, 'game/delete-game.html', context)