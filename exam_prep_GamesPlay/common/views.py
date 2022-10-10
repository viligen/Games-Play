from django.shortcuts import render

from exam_prep_GamesPlay.common.utils import get_profile
from exam_prep_GamesPlay.game.models import Game


# Create your views here.


def index(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'common/home-page.html', context)


def dashboard(request):
    profile = get_profile()
    games = Game.objects.filter(owner_id=profile.id)

    context = {
        'games': games,
        'profile': profile
    }
    return render(request, 'common/dashboard.html', context)