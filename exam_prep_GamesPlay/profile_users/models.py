from django.db import models

from exam_prep_GamesPlay import validators


# Create your models here.


class Profile(models.Model):
    MAX_LEN = 30
    email = models.EmailField()

    age = models.PositiveIntegerField(
        validators=(validators.validate_age, )
    )

    password = models.CharField(
        max_length=MAX_LEN,
    )

    first_name = models.CharField(
        max_length=MAX_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'.strip()
        elif self.first_name:
            return f'{self.first_name}'.strip()
        elif self.last_name:
            return f'{self.last_name}'.strip()
        return None