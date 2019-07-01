from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    has_subscription = models.BooleanField(default=False)

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    text = models.TextField(verbose_name='Текст')
    premium = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
