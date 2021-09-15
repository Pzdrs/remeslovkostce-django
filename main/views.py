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

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object_list.count() >= 1:
            context['category'] = self.object_list.first().category
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-details.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    extra_context = {'catalog': True}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = ProductReview.objects.filter(product_id=self.object.pk)
        return context


class CreateProductReviewView(CreateView):
    template_name = 'create-product-review.html'
    form_class = ProductReviewForm
    extra_context = {'catalog': True}
    product = None

    # when i try to set self.product = Product.objects.get.... in getcontextdata method, the value
    # of self.product is None in get_initial() for some reason so i had to query the db twice here, idk
    # whats up with this thing
    def get_context_data(self, **kwargs):
        print("get_context_data")
        self.product = Product.objects.get(slug=self.kwargs['product_slug'])
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(slug=self.kwargs['product_slug'])
        return context

    def get_initial(self):
        print("get_initial")
        print(self.product)
        initial = super().get_initial()
        initial['product'] = Product.objects.get(slug=self.kwargs['product_slug']).pk
        return initial
