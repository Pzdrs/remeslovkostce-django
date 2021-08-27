from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import ProductCategory, Product


# Create your views here.

def index(request):
    return render(request, 'index.html', {'index': True})


def contact(request):
    return render(request, 'contact.html', {'contact': True})


def catalog(request):
    return render(request, 'catalog.html', {'catalog': True, 'categories': ProductCategory.objects.all()})


def category_details(request, category_slug):
    try:
        category = ProductCategory.objects.get(slug=category_slug)
        products = Product.objects.filter(category_id=category.id)
        return render(request, 'category.html', {'catalog': True, 'category': category, 'products': products})
    except ObjectDoesNotExist as e:
        return render(request, 'error.html', {'message': 'Tento produkt neexistuje'})
