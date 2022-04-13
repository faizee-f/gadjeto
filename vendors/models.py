from django.db import models

# Create your models here.
from account.models import Account

# Create your models here.
class Vendors(models.Model):
    vendor_id = models.OneToOneField(
        Account, on_delete=models.CASCADE, primary_key=True
    )
    brand_name = models.CharField(max_length=60, unique=True)
    tagline = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to="photos/logo", blank=True)
    description = models.TextField(max_length=200, blank=True)

    class Meta:
        ordering = ["brand_name"]

    def __str__(self):
        return self.brand_name
