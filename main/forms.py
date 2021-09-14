from django import forms

from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = "__all__"
        widgets = {
            'product': forms.HiddenInput,
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Hodnocení produktu'}),
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
