from django.urls import reverse
from django.db import models

from account.models import Account

ADD_TYPE = (
    ("Home", "Home"),
    ("Word", "Work"),
)


class Address(models.Model):

    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    add_type = models.CharField(max_length=50, choices=ADD_TYPE)

    def __str__(self):
        return self.first_name


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(
        max_length=10,
        blank=False,
        null=True,
        choices=[("MALE", "MALE"), ("FEMALE", "FEMALE")],
    )
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    profile_picture = models.ImageField(upload_to="user/profile")

    def __str__(self):
        return self.first_name
