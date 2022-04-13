from django import forms
from django.db import models
from django.db.models import fields
from .models import category, sub_category


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ("category_name", "slug", "cat_image")

    def __init__(self, *args, **kwargs):
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class AddSubcategoryForm(forms.ModelForm):
    class Meta:
        model = sub_category
        fields = ("category", "sub_category_name", "slug")

    def __init__(self, *args, **kwargs):
        super(AddSubcategoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
