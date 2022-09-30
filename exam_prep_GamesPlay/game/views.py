from django.shortcuts import render

# Create your views here.


def create_game(request):
    return render(request, 'game/create-game.html')


def details_game(request, id):
    return render(request, 'game/details-game.html')


def edit_game(request, id):
    return render(request, 'game/edit-game.html')


def delete_game(request, id):
    return render(request, 'game/delete-game.html')