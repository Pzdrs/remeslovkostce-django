from django.views.generic import TemplateView, ListView, DetailView

from .models import ProductCategory, Product


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'index': True}


class ContactView(TemplateView):
    template_name = 'contact.html'
    extra_context = {'contact': True}


class CatalogListView(ListView):
    model = ProductCategory
    template_name = 'catalog.html'
    context_object_name = 'categories'
    extra_context = {'catalog': True}


class CategoryProductsView(ListView):
    template_name = 'category.html'
    context_object_name = 'products'
    extra_context = {'catalog': True}

    error_message = None
    category = None

    def get_queryset(self):
        try:
            self.category = ProductCategory.objects.get(slug=self.kwargs['category_slug'])
            return Product.objects.filter(category_id=self.category.id)
        except ProductCategory.DoesNotExist:
            self.error_message = 'Tato kategorie produktů neexistuje'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['error_message'] = self.error_message
        return context


class ProductDetailView(DetailView):
    template_name = 'product_details.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    extra_context = {'catalog': True}

    category = None
    error_message = None

    def get_object(self, queryset=None):
        try:
            self.category = ProductCategory.objects.get(slug=self.kwargs['category_slug'])
            return Product.objects.get(slug=self.kwargs['product_slug'])
        except Product.DoesNotExist:
            self.error_message = 'Tento produkt neexistuje'
        except ProductCategory.DoesNotExist:
            self.error_message = 'Tato kategorie produktů neexistuje'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['error_message'] = self.error_message
        context['category'] = self.category
        return context
