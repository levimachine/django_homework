from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=120, verbose_name='страна', **NULLABLE)
    avatar = models.ImageField(upload_to='media/users/', verbose_name='изображение', **NULLABLE)
    secret_key = models.CharField(max_length=6, verbose_name='секретный ключ(почты)', **NULLABLE)
    user_input_secret_key = models.CharField(max_length=6, verbose_name='секретный ключ', **NULLABLE)
    is_verify = models.BooleanField(default=False, verbose_name='Верификация', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
