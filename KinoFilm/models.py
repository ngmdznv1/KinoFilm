from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=50, verbose_name='Название категории')

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class VideoContent(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название фильма')
    description = models.TextField(verbose_name='Описание фильма')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Картинка')
    video = models.FileField(upload_to='videos/', null=True, blank=True, verbose_name='Видео')
    created_at = models.CharField(max_length=100, verbose_name='Дата выхода')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)
    views = models.ManyToManyField('Ip', related_name="post_views", blank=True, null=True, verbose_name='Просмотры')

    def __str__(self):
        return self.name

    def total_views(self):
        return self.views.count()

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def get_image(self):
        if self.image:
            try:
                return self.image.url
            except:
                return 'https://sun9-66.userapi.com/impg/FAo67kSqOWhv87JEDG4ZPjZ7Pw5TU1Gi0ifp5g/Lgh0Og8QxtU.jpg?size=604x340&quality=95&sign=d1e45dbbe343e46ff2d52cabc4cc4302&type=album'
        else:
            return 'https://sun9-66.userapi.com/impg/FAo67kSqOWhv87JEDG4ZPjZ7Pw5TU1Gi0ifp5g/Lgh0Og8QxtU.jpg?size=604x340&quality=95&sign=d1e45dbbe343e46ff2d52cabc4cc4302&type=album'

    def get_video(self):
        if self.video:
            try:
                return self.video.url
            except:
                return ''
        else:
            return ''


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    content = models.ForeignKey(VideoContent, on_delete=models.CASCADE, verbose_name='Контент')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')

    def __str__(self):
        return f'Комментарий на видео {self.content.name} от пользователя {self.user.username}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    profile_name = models.CharField(max_length=150, default='user', null=True, blank=True,
                                    verbose_name='Имя пользователя')
    nickname = models.CharField(max_length=150, default='@user', null=True, blank=True, verbose_name='Никнейм')
    avatar = models.ImageField(upload_to='profiles/', null=True, blank=True, verbose_name='Фото профиля')

    def __str__(self):
        return f'Профиль пользовател {self.user.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def get_avatar(self):
        if self.avatar:
            try:
                return self.avatar.url
            except:
                return 'https://cs6.pikabu.ru/avatars/43/x43893-1120683787.png'
        else:
            return 'https://cs6.pikabu.ru/avatars/43/x43893-1120683787.png'


class Ip(models.Model):  # наша таблица где будут айпи адреса
    ip = models.CharField(max_length=100, verbose_name='IP пользователя')


def __str__(self):
    return self.ip
