from django import forms

from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = "__all__"
        widgets = {
            'product': forms.HiddenInput,
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0% - 100%'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Obsah recenze'})
        }
