from django.shortcuts import render
from .models import ProductCategory


# Create your views here.

def index(request):
    return render(request, 'index.html', {'index': True})


def contact(request):
    return render(request, 'contact.html', {'contact': True})


def catalog(request):
    return render(request, 'catalog.html', {'catalog': True, 'categories': ProductCategory.objects.all()})


def category_details(request, category_slug):
    category = ProductCategory.objects.get(slug=category_slug)
    return render(request, 'category.html', {'catalog': True, 'category': category})
