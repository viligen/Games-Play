from django.shortcuts import render, redirect

from exam_prep_GamesPlay.common.utils import get_profile
from exam_prep_GamesPlay.game.models import Game
from exam_prep_GamesPlay.profile_users.forms import CreatProfile, DeleteProfile, EditProfile
from exam_prep_GamesPlay.profile_users.models import Profile


# Create your views here.


def create_profile(request):
    form = CreatProfile()
    if request.method == 'POST':
        form = CreatProfile(request.POST)
        form.full_clean()
        if form.is_valid():
            form.save()

            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.all()[0]
    # games = Game.objects.filter(owner_id=profile.id)
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
    profile = get_profile()
    form = EditProfile(instance=profile)

    if request.method == 'POST':
        form = EditProfile(request.POST, instance=profile)
        form.full_clean()
        if form.is_valid():
            form.save()

            return redirect('details profile')
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    form = DeleteProfile(instance=profile)
    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    context = {
        'profile': profile,
        'form': form,

    }

    return render(request, 'profile/delete-profile.html', context)