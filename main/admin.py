from django.contrib import admin
from . import models


# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'thumbnail')
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'image')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category', 'image')


admin.site.register(models.ProductCategory, ProductCategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductReview)
