from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, DateTimeField
from account.models import Account
from category.models import category, sub_category
from store.models import Variation, product
from vendors.models import Vendors

# Create your models here.
    
class CategoryOffer(models.Model):
    category_name=models.OneToOneField(category,on_delete=models.CASCADE)
    offer=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    is_valid=BooleanField(default=True)

    def __int__(self):
        return self.category_name

class SubCategoryOffer(models.Model):
    subcategory_name=models.OneToOneField(sub_category,on_delete=models.CASCADE)
    offer=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    is_valid=BooleanField(default=True)

    def __int__(self):
        return self.subcategory_name

class VendorOffer(models.Model):
    vendor_name=models.OneToOneField(Vendors,on_delete=models.CASCADE)
    offer=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    is_valid=BooleanField(default=True)

    def __int__(self):
        return self.vendor_name

class ProductOffer(models.Model):
    product_name=models.OneToOneField(product,on_delete=models.CASCADE)
    offer=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    is_valid=BooleanField(default=True)

    def __int__(self):
        return self.product_name

class VariationOffer(models.Model):
    variation_name=models.OneToOneField(Variation,on_delete=models.CASCADE)
    offer=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    is_valid=BooleanField(default=True)

    def __int__(self):
        return self.variation_name




class Coupen(models.Model):
    coupen_code=models.CharField(max_length=100,unique=True)
    coupen_count=models.IntegerField()
    valid_from=models.DateField()
    valid_to=models.DateField()
    discount=models.IntegerField()
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models,DateTimeField(auto_now=True)


    def __int__(self):
        return self.coupen_code

class RedeemedCoupen(models.Model):
    coupen=models.ForeignKey(Coupen,on_delete=models.CASCADE)
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models,DateTimeField(auto_now=True)

    def __int__(self):
        return self.coupen