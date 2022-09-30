from django.urls import path

from exam_prep_GamesPlay.common.views import dashboard, index

urlpatterns = [
    path('', index, name='home'),
    path('dashboard/', dashboard, name='dashboard')

]