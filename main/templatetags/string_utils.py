from django import template

register = template.Library()


@register.filter(is_safe=True)
def description(product, max_length):
    if len(product.description) > max_length:
        return f'{product.description[:max_length]}...<a href="{product.get_absolute_url()}">číst dále</a>'
    else:
        return product.description
