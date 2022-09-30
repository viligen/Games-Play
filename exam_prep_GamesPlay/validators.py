from django.core.exceptions import ValidationError

MIN_AGE = 12

MIN_RATING = 0.1
MAX_RATING = 5.0

MIN_FOR_MAX_LEVEL = 1


def validate_age(value):
    if value < MIN_AGE:
        raise ValidationError(f' age: {value} is less than minimum age: {MIN_AGE}')


def validate_rating(value):
    if value < MIN_RATING or value > MAX_RATING:
        raise ValidationError(f' rating: {value} must be between {MIN_RATING} and {MAX_RATING}')


def validate_max_level(value):
    if value < MIN_FOR_MAX_LEVEL:
        raise ValidationError(f' Max level: {value} is less than required minimum: {MIN_FOR_MAX_LEVEL}')