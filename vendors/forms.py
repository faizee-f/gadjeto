from django import forms
from django.db import models
from django.db.models import fields
from .models import Vendors


class RegisterVendor(forms.ModelForm):
    class Meta:
        model = Vendors
        fields = ("brand_name", "tagline", "logo", "description")

    def __init__(self, *args, **kwargs):
        super(RegisterVendor, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'