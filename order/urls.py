from os import name

from myproject.settings import MEDIA_ROOT
from . import views
from django.urls import path
from django.conf import settings


urlpatterns = [
    path("place_order", views.place_order, name="place_order"),
    path("payments", views.payments, name="payments"),
    path("order_complete/", views.order_complete, name="order_complete"),
    path("paymenthandler/", views.paymenthandler, name="paymenthandler"),
    path("cash_on_delivery/", views.cash_on_delivery, name="cash_on_delivery"),
]
