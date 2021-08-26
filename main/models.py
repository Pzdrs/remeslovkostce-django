from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    thumbnail = models.ImageField

    def __str__(self):
        return self.name


