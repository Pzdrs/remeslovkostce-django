from django import forms

from . import models


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = models.ProductReview
        fields = "__all__"
        widgets = {
            'product': forms.HiddenInput,
            'rating': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Hodnocení produktu', 'min': 0, 'max': 100, 'value': 0}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Obsah recenze'})
        }
        labels = {
            'rating': 'Hodnocení produktu',
            'content': 'Obsah recenze'
        }
        help_texts = {
            'rating': 'Hodnocení od 1% do 100%'
        }
        error_messages = {
            'rating': {
                'min_value': 'Hodnocení produktu musí být mezi 1%% - 100%%',
                'max_value': 'Hodnocení produktu musí být mezi 1%% - 100%%'
            },
            'content': {
                'required': 'Obsah recenze nesmí být prázdný'
            }
        }


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['category', 'name', 'slug', 'description', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Název produktu'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug produktu'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Popis produktu'}),
        }
        labels = {
            'category': 'Kategorie',
            'name': 'Název produktu',
            'description': 'Popis produktu',
            'image': 'Foto produktu'
        }


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['category', 'name', 'slug', 'description', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select', 'disabled': True}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Název produktu'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug produktu'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Popis produktu'}),
        }
        labels = {
            'category': 'Kategorie',
            'name': 'Název produktu',
            'description': 'Popis produktu',
            'image': 'Foto produktu'
        }
