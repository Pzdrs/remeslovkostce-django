from django.contrib import admin
from . import models


# Register your models here.

class MainAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.ProductCategory, MainAdmin)
