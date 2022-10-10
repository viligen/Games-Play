from django import forms

from exam_prep_GamesPlay.profile_users.models import Profile


class DeleteProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreatProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        # extra_kwargs = {'password': {'write_only': True}}
        widgets = {
            'password': forms.PasswordInput()
        }