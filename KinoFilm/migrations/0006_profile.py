# Generated by Django 5.1.4 on 2025-01-07 14:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KinoFilm', '0005_remove_profile_user_delete_favoritemovie_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(blank=True, default='user', max_length=150, null=True, verbose_name='Имя пользователя')),
                ('nickname', models.CharField(blank=True, default='@user', max_length=150, null=True, verbose_name='Никнейм')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='profiles/', verbose_name='Фото профиля')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
