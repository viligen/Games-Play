from django.shortcuts import render

from exam_prep_GamesPlay.game.models import Game
from exam_prep_GamesPlay.profile_users.models import Profile


# Create your views here.


def create_profile(request):

    return render(request, 'profile/create-profile.html')


def details_profile(request):
    profile = Profile.objects.all()[0]
    games = Game.objects.all()
    games_count = len(games)
    average_rating = sum([g.rating for g in games])/games_count if games_count > 0 else 0
    context = {
        'profile': profile,
        'games_count': games_count,
        'average_rating': average_rating,
    }
    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')