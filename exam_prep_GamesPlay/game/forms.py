from django import forms

from exam_prep_GamesPlay.game.models import Game


class CreateGame(forms.ModelForm):
    class Meta:
        model = Game
        # profile = get_profile()
        # owner = profile.id

        exclude = ('owner',)

        labels = {
            'max_level': 'Max Level',
        }


class EditGame(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('owner',)


class DeleteGame(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('owner',)