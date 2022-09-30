# Generated by Django 4.1.1 on 2022-10-07 12:15

from django.db import migrations, models
import exam_prep_GamesPlay.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('category', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Puzzle', 'Puzzle'), ('Strategy', 'Strategy'), ('Sports', 'Sports'), ('Board/Card Game', 'Board/Card Game'), ('Other', 'Other')], max_length=15)),
                ('rating', models.FloatField(validators=[exam_prep_GamesPlay.validators.validate_rating])),
                ('max_level', models.PositiveIntegerField(blank=True, null=True, validators=[exam_prep_GamesPlay.validators.validate_max_level])),
                ('image_URL', models.URLField()),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
