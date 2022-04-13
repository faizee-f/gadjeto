from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from account.models import Account
from store.models import Variation, product
from vendors.models import Vendors

# Create your models here.


class Payment(models.Model):

    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.payment_id


class Order(models.Model):
    STATUS = (
        ("New", "New"),
        ("Accepted", "Accepted"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    )

    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, blank=True, null=True
    )
    order_number = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    order_note = models.CharField(max_length=200, blank=True)
    order_total = models.FloatField()
    tax = models.FloatField()
    coupon_redeemed = models.IntegerField(blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=20, default="New")
    ip = models.CharField(blank=True, max_length=20)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def full_address(self):
        return f"{self.address1} {self.address2}"

    def __str__(self):
        return self.first_name


class OrderProduct(models.Model):
    STATUS = (
        ("New", "New"),
        ("Accepted", "Accepted"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(
        Payment, on_delete=models.SET_NULL, blank=True, null=True
    )
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=20, default="New")
    products = models.ForeignKey(product, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    test = models.CharField(max_length=100, blank=True)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.products.product_name

    def sub_total(self):
        return self.quantity * self.price

    def varient_tax(self):
        return self.sub_total() * 2 / 100

    def grand_total(self):
        return self.sub_total() + self.varient_tax()
