from django import forms
from django.forms import HiddenInput
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['product', 'rating', 'content']
        widgets = {
            'product': HiddenInput
        }
