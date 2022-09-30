from django.contrib import admin

from exam_prep_GamesPlay.profile_users.models import Profile


# Register your models here.

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass