from os import name
from myproject.settings import MEDIA_ROOT
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.vendor_signin,name='vendor_signin'),
    path('vendor_home',views.vendor_home, name='vendor_home'),
    path('vendor_signup',views.vendor_signup,name='vendor_signup'),
    path('vendor_signout',views.vendor_signout,name='vendor_signout' ),
    path('vendor_profile',views.vendor_profile,name='vendor_profile'),

    path('add_product',views.add_product,name="add_product"),
    path('view_product',views.view_product,name="view_product"),

    
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
