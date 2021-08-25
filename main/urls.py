from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('katalog/', views.catalog, name='catalog'),
    path('kontakt/', views.contact, name='contact'),
]
