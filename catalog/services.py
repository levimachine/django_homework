from django.core.cache import cache

from logger import logger
from catalog.models import Product
from config import settings


def get_cached_category_products(category):
    if settings.CACHE_ENABLE:
        key = f'products_{category.name}'
        cache_data = cache.get(key)
        if cache_data is None:
            product_list = Product.objects.filter(category=category)
            cache.set(key, product_list)
            products = product_list
            logger.info('Берёт данные из бд')
        else:
            products = cache_data
            logger.info('Берёт данные из кеша')
    else:
        products = Product.objects.filter(category=category)
    return products
