# Generated by Django 4.1.1 on 2022-10-10 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_users', '0001_initial'),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='owner_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profile_users.profile'),
        ),
    ]
