from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView

from .models import ProductCategory, Product


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {'index': True}


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        return {'contact': True}


class CatalogView(TemplateView):
    template_name = 'catalog.html'

    def get_context_data(self, **kwargs):
        return {'catalog': True, 'categories': ProductCategory.objects.all()}


class CategoryDetailsView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        try:
            category = ProductCategory.objects.get(slug=self.kwargs['category_slug'])
            products = Product.objects.filter(category_id=category.id)
            return {'catalog': True, 'category': category, 'products': products}
        except ObjectDoesNotExist:
            self.template_name = 'error.html'
            return {'catalog': True, 'message': 'Tento produkt neexistuje'}
