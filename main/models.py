from django.db import models
from django.urls import reverse


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images', default='not-found.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:category_details', args=(self.slug,))


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/products', default='not-found.jpg')
    stars = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_details', args=(self.category.slug, self.slug))
