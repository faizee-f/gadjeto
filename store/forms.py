from django.db.models.deletion import CASCADE
from .models import product
from django import forms
from django.db import models
from django.db.models import fields
from store.models import product
from category.models import category

class AddProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ("category","vendor","product_name","slug","description","image1","image2","image3")

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

# class AddVarientCategoryForm(forms.ModelForm):

#     class Meta:
#         model = VariationCategories
#         fields = ("var_category", "name", "slug")

#     def __init__(self, *args, **kwargs):
#         super(AddVarientCategoryForm, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'

# class AddVarientItemForm(forms.ModelForm):
#     class Meta:
#         model = VariationItems
#         fields = ("item_category", "name", "slug")

#     def __init__(self, *args, **kwargs):
#         super(AddVarientItemForm, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'


# class VariationsForm(forms.ModelForm):

#     class Meta:
#         model = Variations
#         fields = ("item_category", "name", "slug")

#     def __init__(self, *args, **kwargs):
#         super(VariationsForm, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'
