from django.db import models
from config.settings import AUTH_USER_MODEL

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    # create_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        db_table = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='media/', verbose_name='Изображение')
    category = models.ForeignKey(Category, to_field='id', on_delete=models.CASCADE, verbose_name='Категория')
    is_published = models.CharField(default='not_published',  choices=[('published', 'Да'), ('not_published', 'Нет')], verbose_name='Опубликовано')
    price_per_piece = models.IntegerField(verbose_name='Цена за штуку')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    user = models.ForeignKey(AUTH_USER_MODEL, default=True, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        db_table = 'products'
        permissions = [('catalog.set_published_status_product', 'Can publish продукт'), ]


"""заголовок,
slug (реализовать через CharField),
содержимое,
превью (изображение),
дата создания,
признак публикации,
количество просмотров."""


class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    slug = models.CharField(max_length=150, verbose_name='slug')
    preview = models.ImageField(upload_to='media/', verbose_name='Превью изображение')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    is_published = models.CharField(default=True,
                                    choices=[('published', 'Да'), ('not_published', 'Нет')],
                                    verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    user = models.ForeignKey(AUTH_USER_MODEL,  default=True, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='id', verbose_name='Продукт')
    number = models.IntegerField(verbose_name='Номер версии')
    title = models.CharField(max_length=150,  verbose_name='Название версии')
    is_actual = models.CharField(choices=[('actual', 'Актуальная'), ('not_actual', 'Не уктуальная')],
                                 verbose_name='Актуальность версии')

    def __str__(self):
        return f'{self.title}, {self.number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

