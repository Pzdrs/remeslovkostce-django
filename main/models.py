from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
from django.utils import timezone


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images', default='not-found.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:category_details', args=(self.slug,))


class ProductReview(models.Model):
    published = models.DateField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    content = models.TextField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.published = timezone.now()
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return str(self.rating)


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/products', default='not-found.jpg')
    reviews = models.ManyToManyField(ProductReview)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_details', args=(self.category.slug, self.slug))
