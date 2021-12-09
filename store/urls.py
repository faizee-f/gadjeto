from os import name

from django.urls.conf import include
from myproject.settings import MEDIA_ROOT
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.shop,name='shop'),
    path('category/<slug:category_slug>/',views.shop,name='product_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/<slug:varient_slug>',views.product_detail,name='product_detail'),
    path('search/',views.search,name='search'),
    
    path('submit_review/<varient_id>',views.submit_review,name='submit_review'),
    path('quick_buy/<id>',views.quick_buy,name='quick_buy'),
]
