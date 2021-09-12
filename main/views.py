from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import *

from .models import ProductCategory, Product, ProductReview
from .forms import ProductReviewForm


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


class ProductDetailView(DetailView, BaseCreateView):
    template_name = 'product_details.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    extra_context = {'catalog': True}
    form_class = ProductReviewForm

    category = None
    reviews = None
    error_message = None

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def get_object(self, queryset=None):
        try:
            self.category = ProductCategory.objects.get(slug=self.kwargs['category_slug'])
            product = Product.objects.get(slug=self.kwargs[self.slug_url_kwarg])
            self.reviews = ProductReview.objects.filter(product=product.pk)
            return product
        except Product.DoesNotExist:
            self.error_message = 'Tento produkt neexistuje'
        except ProductCategory.DoesNotExist:
            self.error_message = 'Tato kategorie produktů neexistuje'

    def get_initial(self):
        initial = super().get_initial()
        if self.get_object():
            initial['product'] = self.get_object().pk
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['error_message'] = self.error_message
        context['category'] = self.category
        context['reviews'] = self.reviews
        return context
