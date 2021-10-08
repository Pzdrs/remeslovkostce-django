from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def description(product, max_length):
    if len(product.description) > max_length:
        return mark_safe(f'{product.description[:max_length]}...<a href="{product.get_absolute_url()}">číst dále</a>')
    else:
        return product.description


