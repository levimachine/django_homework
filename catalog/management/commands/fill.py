from django.db import connection
from django.core.management import BaseCommand
import json
from catalog.models import Category, Product
from config.settings import BASE_DIR

FIXTURES_DIR = BASE_DIR / 'catalog' / 'fixtures'


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Удаляем все модели из базы данных
        Product.objects.all().delete()
        Category.objects.all().delete()
        # Сбрасываем автоинкремент до 1 в двух таблицах.
        with connection.cursor() as cur:
            for seq in ['products_id_seq', 'categories_id_seq']:
                cur.execute(f'ALTER SEQUENCE {seq} RESTART WITH 1;')
        # Добавляем категории из json файла.
        with open(f'{FIXTURES_DIR / 'categories.json'}', 'r', encoding='utf-8') as f:
            data = json.load(f)
            categories = []
            for category in data:
                categories.append(Category(**category['fields']))
            Category.objects.bulk_create(categories)
        # Добавляем продукты из json файла.
        with open(f'{FIXTURES_DIR / 'products.json'}', 'r', encoding='utf-8') as f:
            data = json.load(f)
            products = []
            for product in data:
                #Модель Product ожидает получить в поле category объект Category, а не его id(pk), поэтому по id преобразовываем его в модель Category.
                category_id = product['fields']['category']
                product['fields']['category'] = Category.objects.get(pk=category_id)
                products.append(Product(**product['fields']))
            Product.objects.bulk_create(products)
