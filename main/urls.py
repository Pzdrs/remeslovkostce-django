from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('kontakt/', views.ContactView.as_view(), name='contact'),
    path('katalog/', views.CatalogListView.as_view(), name='catalog'),
    path('katalog/<slug:category_slug>/', views.CategoryProductsView.as_view(), name='category_details'),
    path('katalog/<slug:category_slug>/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_details')
]
