# Generated by Django 4.1.1 on 2022-10-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.URLField(blank=True, null=True, verbose_name='Profile Picture'),
        ),
    ]