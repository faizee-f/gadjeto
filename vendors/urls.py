from os import name
from myproject.settings import MEDIA_ROOT
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.vendor_signin, name='vendor_signin'),
    path('vendor_home', views.vendor_home, name='vendor_home'),
    path('vendor_signup', views.vendor_signup, name='vendor_signup'),
    path('vendor_signout', views.vendor_signout, name='vendor_signout'),
    path('vendor_profile', views.vendor_profile, name='vendor_profile'),


    path('view_product', views.view_product, name="view_product"),
    path('add_product', views.add_product, name="add_product"),
    path('edit_product/<id>', views.edit_product, name="edit_product"),
    path('activate_product/<id>', views.activate_product, name="activate_product"),
    path('delete_product/<id>', views.delete_product, name="delete_product"),

    path('varient_list', views.varient_list, name="varient_list"),
    path('view_varient/<id>', views.view_varient, name="view_varient"),
    path('add_varient/<id>', views.add_varient, name="add_varient"),
    path('edit_varient/<id>', views.edit_varient, name="edit_varient"),
    path('activate_varient/<id>', views.activate_varient, name="activate_varient"),
    path('delete_varient/<id>', views.delete_varient, name="delete_varient"),

    path('view_order', views.view_order, name="view_order"),
    path('view_order_detail/<order_id>',
         views.view_order_detail, name="view_order_detail"),

    path('view_offers', views.view_offers, name="view_offers"),
    path('edit_varient_offers/<id>', views.edit_varient_offers,
         name="edit_varient_offers"),
    path('edit_product_offers/<id>', views.edit_product_offers,
         name="edit_product_offers"),
    path('edit_vendor_offers/<id>', views.edit_vendor_offers,
         name="edit_vendor_offers"),
    
    path('delete_product_offer/<id>', views.delete_product_offer,
         name="delete_product_offer"),
    path('delete_variation_offer/<id>', views.delete_variation_offer,
         name="delete_variation_offer"),

    path('activate_product_offer/<id>', views.activate_product_offer,
         name="activate_product_offer"),
    path('activate_variation_offer/<id>', views.activate_variation_offer,
         name="activate_variation_offer"),

    path('add_product_offer',views.add_product_offer,name="add_product_offer"),
    path('add_variation_offer',views.add_variation_offer,name="add_variation_offer"),

    #report generation

    path('product_report',views.product_report,name="product_report"),
    path('product_export_csv',views.product_export_csv,name="product_export_csv"),
    path('product_export_pdf',views.product_export_pdf,name="product_export_pdf"),
    path('orders_export_csv',views.orders_export_csv,name="orders_export_csv"),
    path('orders_export_pdf',views.orders_export_pdf,name="orders_export_pdf"),
    path('sales_export_csv',views.sales_export_csv,name="sales_export_csv"),
    path('sales_export_pdf',views.sales_export_pdf,name="sales_export_pdf"),
    
    
    path('order_shipped/<id>',views.order_shipped,name="order_shipped"),
    path('order_delivered/<id>',views.order_delivered,name="order_delivered"),
    path('order_cancelled/<id>',views.order_cancelled,name="order_cancelled"),
    path('order_history',views.order_history,name='order_history'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
