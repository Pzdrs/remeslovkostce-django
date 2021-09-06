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
    model = ProductCategory
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['catalog'] = True
        return context


class CategoryDetailsView(ListView):
    template_name = 'category.html'
    context_object_name = 'products'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_message = None
        self.category = None

    def get_queryset(self):
        try:
            self.category = ProductCategory.objects.get(slug=self.kwargs['category_slug'])
            return Product.objects.filter(category_id=self.category.id)
        except ObjectDoesNotExist:
            self.error_message = 'Tento produkt neexistuje'
            self.template_name = 'error.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalog'] = True
        context['category'] = self.category
        context['message'] = self.error_message
        return context
