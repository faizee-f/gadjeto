from django import forms
from django.db import models
from django.forms import fields, widgets

from offer.models import (
    CategoryOffer,
    Coupen,
    ProductOffer,
    SubCategoryOffer,
    VariationOffer,
    VendorOffer,
)
from store.models import Variation, product
from vendors.models import Vendors


class CategoryOfferForm(forms.ModelForm):
    class Meta:
        model = CategoryOffer
        fields = ("category_name", "offer", "is_valid")

    def __init__(self, *args, **kwargs):
        super(CategoryOfferForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class SubCategoryOfferForm(forms.ModelForm):
    class Meta:
        model = SubCategoryOffer
        fields = ("subcategory_name", "offer", "is_valid")

    def __init__(self, *args, **kwargs):
        super(SubCategoryOfferForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class VendorOfferForm(forms.ModelForm):
    class Meta:
        model = VendorOffer
        fields = ("vendor_name", "offer", "is_valid")

    def __init__(self, vendor_id=None, **kwargs):
        super(VendorOfferForm, self).__init__(**kwargs)
        if vendor_id:
            self.fields["vendor_name"].queryset = Vendors.objects.filter(
                vendor_id=vendor_id
            )
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class ProductOfferForm(forms.ModelForm):
    class Meta:
        model = ProductOffer
        fields = ("product_name", "offer", "is_valid")

    def __init__(self, vendor_id=None, **kwargs):
        super(ProductOfferForm, self).__init__(**kwargs)
        if vendor_id:
            self.fields["product_name"].queryset = product.objects.filter(
                vendor_id=vendor_id
            )
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class VariationOfferForm(forms.ModelForm):
    class Meta:
        model = VariationOffer
        fields = ("variation_name", "offer", "is_valid")

    def __init__(self, vendor_id=None, **kwargs):
        super(VariationOfferForm, self).__init__(**kwargs)
        if vendor_id:
            self.fields["variation_name"].queryset = Variation.objects.filter(
                product__vendor_id=vendor_id
            )
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class DateInput(forms.DateInput):
    input_type = "date"


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupen
        fields = (
            "coupen_code",
            "coupen_count",
            "discount",
            "valid_from",
            "valid_to",
        )
        widgets = {
            "valid_from": DateInput(),
            "valid_to": DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CouponForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
