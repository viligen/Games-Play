from django.contrib import admin

from exam_prep_GamesPlay.game.models import Game


# Register your models here.


@admin.register(Game)
class AdminGame(admin.ModelAdmin):
    pass