from django.shortcuts import get_object_or_404
from django.views import generic

from .models import *
from . import forms


# Create your views here.

class Index(generic.TemplateView):
    template_name = 'index.html'
    extra_context = {'index': True}


class Contact(generic.TemplateView):
    template_name = 'contact.html'
    extra_context = {'contact': True}


class Catalog(generic.ListView):
    model = ProductCategory
    template_name = 'catalog.html'
    context_object_name = 'categories'
    extra_context = {'catalog': True}


class CategoryProducts(generic.ListView):
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


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'product-details.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    extra_context = {'catalog': True}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = ProductReview.objects.filter(product_id=self.object.pk)
        return context


class CreateProduct(generic.CreateView):
    model = Product
    form_class = forms.CreateProductForm
    template_name = 'create-product.html'

    extra_context = {'catalog': True}

    category = None

    def get_context_data(self, **kwargs):
        self.category = get_object_or_404(ProductCategory, slug=self.kwargs['category_slug'])
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

    def get_initial(self):
        if self.category is None:
            self.category = get_object_or_404(ProductCategory, slug=self.kwargs['category_slug'])
        initial = super().get_initial()
        initial['category'] = self.category.pk
        return initial


class UpdateProduct(generic.UpdateView):
    model = Product
    form_class = forms.UpdateProductForm
    template_name = 'update-product.html'
    slug_url_kwarg = 'product_slug'

    extra_context = {'catalog': True}


class DeleteProduct(generic.DeleteView):
    model = Product
    template_name = 'delete-product.html'
    slug_url_kwarg = 'product_slug'

    extra_context = {'catalog': True}

    def get_success_url(self):
        return self.object.category.get_absolute_url()


class CreateProductReview(generic.CreateView):
    model = ProductReview
    form_class = forms.ProductReviewForm
    template_name = 'create-product-review.html'

    extra_context = {'catalog': True}

    product = None

    def get_context_data(self, **kwargs):
        self.product = Product.objects.get(slug=self.kwargs['product_slug'])
        context = super().get_context_data(**kwargs)
        context['product'] = self.product
        return context

    def get_initial(self):
        if self.product is None:
            self.product = Product.objects.get(slug=self.kwargs['product_slug'])
        initial = super().get_initial()
        initial['product'] = self.product.pk
        return initial
