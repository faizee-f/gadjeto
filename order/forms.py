from django import forms
from django.db.models.base import Model
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields=['first_name','last_name','phone','email','address1','address2','country','state','city','pincode','order_note']
