from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView

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


class CatalogListView(ListView):
    template_name = 'catalog.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return ProductCategory.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['catalog'] = True
        return context


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
