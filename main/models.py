from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
from django.utils import timezone


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='images', default='not-found.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:category-details', args=(self.slug,))


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/products', default='not-found.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product-details', args=(self.category.slug, self.slug))


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    published = models.DateField(auto_now_add=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    content = models.TextField()

    def __str__(self):
        return str(self.rating)

    def get_absolute_url(self):
        return f'{self.product.get_absolute_url()}#{self.pk}'
