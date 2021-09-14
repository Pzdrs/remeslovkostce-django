from django.urls import reverse
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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    extra_context = {'catalog': True}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = ProductReview.objects.filter(product_id=self.object.pk)
        return context


class CreateProductReviewView(CreateView):
    template_name = 'create_product_review.html'
    form_class = ProductReviewForm
    extra_context = {'catalog': True}

    # when i try to set self.product = Product.objects.get.... in getcontextdata method, the value
    # of self.product is None in get_initial() for some reason so i had to query the db twice here, idk
    # whats up with this thing
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(slug=self.kwargs['product_slug'])
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['product'] = Product.objects.get(slug=self.kwargs['product_slug']).pk
        return initial
