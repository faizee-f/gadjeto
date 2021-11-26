from os import name

from django.conf.urls import url
from myproject.settings import MEDIA_ROOT
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.admin_signin ,name='admin_signin'),
    path('admin_signout',views.admin_signout,name="admin_signout"),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),

    path('category_list',views.category_list,name='category_list'),
    path('edit_category/<cat_id>',views.edit_category,name='edit_category'),
    path('delete_category/<cat_id>',views.delete_category,name='delete_category'),

    # path('varient_category_list',views.varient_category_list,name='varient_category_list'),
    # path('edit_varient_category/<subcat_id>',views.edit_varient_category,name='edit_varient_category'),
    # path('delete_varient_category/<subcat_id>',views.delete_varient_category,name='delete_varient_category'),

    # path('varient_list',views.varient_list,name='varient_list'),
    # path('edit_varient/<var_id>',views.edit_varient,name='edit_varient'),
    # path('delete_varient/<var_id>',views.delete_varient,name='delete_varient'),


    path('customers',views.customers,name='customers'),
    path('vendor_approval',views.vendor_approval,name='vendor_approval'),
    path('approve_vendor/<vendor_id>',views.approve_vendor,name='approve_vendor'),
    path('reject_vendor/<vendor_id>',views.reject_vendor,name='reject_vendor'),
    path('user_block_unblock/<customer_id>',views.user_block_unblock,name='user_block_unblock'),    
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
