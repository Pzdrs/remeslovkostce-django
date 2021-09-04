from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('', views.IndexView.as_view(), name='index'),
                  path('kontakt/', views.ContactView.as_view(), name='contact'),
                  path('katalog/', views.CatalogView.as_view(), name='catalog'),
                  path('katalog/<slug:category_slug>', views.CategoryDetailsView.as_view(), name='category_details'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
