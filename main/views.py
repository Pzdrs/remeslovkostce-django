from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html', {'index': True})


def catalog(request):
    return render(request, 'catalog.html', {'catalog': True})


def contact(request):
    return render(request, 'contact.html', {'contact': True})
