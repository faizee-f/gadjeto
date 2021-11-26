from os import name

from django.conf.urls import url
from myproject.settings import MEDIA_ROOT
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.cart,name='cart'),
    path('add_cart/<int:product_id>/',views.add_cart,name='add_cart'),
    path('remove_cart/<int:product_id>/',views.remove_cart,name='remove_cart'),
    path('delete_cart/<int:product_id>/',views.delete_cart,name='delete_cart'),
    path('checkout',views.checkout,name='checkout'),
]
