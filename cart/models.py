from django.db import models
from django.db.models.deletion import CASCADE
from account.models import Account
from store.models import Variation, product

# Create your models here.


class Cart(models.Model):

    cart_id = models.CharField(max_length=50, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user=models.ForeignKey(Account,on_delete=CASCADE,null=True)
    varient=models.ForeignKey(Variation,on_delete=CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.varient.price*self.quantity

    def __unicode__(self):
        return self.varient
