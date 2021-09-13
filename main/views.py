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

    # TODO: toto jsem doplnil jako implicitni queryset
    queryset = Product.objects.all()

    def get_success_url(self):
        print("get_success_url")
        return self.get_object().get_absolute_url()

    # TODO: protoze slug jednoznacne definuje produkt, nemusim se nijak zabyvat kategorii
    #  a vlastne i produkt se nacte diky predanym kwargs parametrum implicitne do self.object
    #  takze tato metoda nedela nic potrebneho ci logickeho navic muzeme ji tedy vypustit..
    #  Ano je tam test platnosti slug parametru, ale to lze bezne klidne ignorovat. Pokud by
    #  jste na tom trval pak bych dal ten test do get metody a v pripade chyby bych dal HTTPResponseRedirect
    #  na chybovou hlasku...
    def get_object(self, queryset=None):
        print("get_object")

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
        print("get_initial")
        # TODO: toto sem logicky nepatri, ale je na tom videt z printu na konzoli, ze jde prvni metodu kterou realne
        #  volate Vy (ostatni jako get, post se volaji automaticky). Takze pokud bychom vymazali vasi implementaci
        #  get_object a nechali zavolat implicitne definovanou porad vse bude normalne fungovat, protoze implicitne
        #  DetailView zapise instanci z databaze do self.object - zde to delam rucne pro demonstracni ucely
        #  NAVIC!!! - odpadne neustale volani get_object na ruznych mistech a tudiz neustale dotazy na databazi...
        self.object = super(ProductDetailView, self).get_object(self.queryset)
        initial = super().get_initial()
        if self.get_object():
            initial['product'] = self.get_object().pk
        return initial

    def get_context_data(self, **kwargs):
        print("get_context_data")
        context = super().get_context_data(**kwargs)
        context['error_message'] = self.error_message
        context['category'] = self.category
        context['reviews'] = self.reviews
        return context
