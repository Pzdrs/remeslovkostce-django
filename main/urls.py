from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('kontakt/', views.Contact.as_view(), name='contact'),
    path('katalog/', views.Catalog.as_view(), name='catalog'),
    path('katalog/<slug:category_slug>/', views.CategoryProducts.as_view(), name='category-details'),
    path('katalog/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view(),
         name='product-details'),
    path('katalog/<slug:category_slug>/<slug:product_slug>/review/', views.CreateProductReview.as_view(),
         name='create-product-review'),
    path('katalog/<slug:category_slug>/create', views.CreateProduct.as_view(), name='create-product'),
    path('katalog/<slug:category_slug>/<slug:product_slug>/update/', views.UpdateProduct.as_view(),
         name='update-product'),
    path('katalog/<slug:category_slug>/<slug:product_slug>/delete/', views.DeleteProduct.as_view(),
         name='delete-product'),
]
