from django.shortcuts import render

from exam_prep_GamesPlay.game.models import Game
from exam_prep_GamesPlay.profile_users.models import Profile


# Create your views here.
def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


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