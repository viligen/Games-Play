from django.db import models

from exam_prep_GamesPlay import validators
from exam_prep_GamesPlay.profile_users.models import Profile


# Create your models here.


class Game(models.Model):
    MAX_LEN_TITLE = 30
    MAX_LEN_CATEGORY = 15
    AVAILABLE_CATEGORIES = tuple([(c, c) for c in ["Action", "Adventure", "Puzzle", "Strategy", "Sports",
                                                   "Board/Card Game", "Other"]])
    print(AVAILABLE_CATEGORIES)

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        unique=True,
    )

    category = models.CharField(
        max_length=MAX_LEN_CATEGORY,
        choices=AVAILABLE_CATEGORIES
    )

    rating = models.FloatField(
        validators=(validators.validate_rating, )
    )

    max_level = models.PositiveIntegerField(
        null=True,
        blank=True,

        validators=(validators.validate_max_level, )
    )

    image_URL = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,

    )