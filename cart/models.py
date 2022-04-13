from django.db import models
from django.db.models.deletion import CASCADE
from account.models import Account
from store.models import Variation, product


class Cart(models.Model):

    cart_id = models.CharField(max_length=50, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    varient = models.ForeignKey(Variation, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def total(self):
        if self.varient.offer_price():
            discount_total = 0
            off_price = Variation.offer_price(self.varient)
            discount_total += off_price["new_price"] * self.quantity
            return discount_total
        else:
            return self.varient.price * self.quantity

    def __unicode__(self):
        return self.varient
