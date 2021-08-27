from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kontakt/', views.contact, name='contact'),
    path('katalog/', views.catalog, name='catalog'),
    path('katalog/<slug:category_slug>', views.category_details, name='category_details'),
]


