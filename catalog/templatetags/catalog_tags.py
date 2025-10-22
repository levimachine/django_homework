from django import template

from catalog.models import Product

register = template.Library()


@register.filter('media_path')
def media_path_filter(value: Product):
    if hasattr(value, 'image') and value.image:
        return value.image.url
    return ''

@register.simple_tag
def media_path_tag(value: Product):
    if hasattr(value, 'image') and value.image:
        return value.image.url
    return ''
