from os import name

from django.urls.conf import include
from myproject.settings import MEDIA_ROOT
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name='home'),
    path('signin',views.signin,name='signin'),
    path('forgot_password',views.forgot_password,name="forgot_password"),
    path('register',views.register,name='register'),
    path('register_otp',views.register_otp,name='register_otp'),
    path('signout',views.signout,name='signout'),
    path('signin_otp',views.signin_otp,name='signin_otp'),
    path('otp_validation',views.otp_validation,name='otp_validation'),
    path('forbidden_user',views.forbidden_user,name="forbidden_user"),
    path('resend_otp',views.resend_otp,name='resend_otp'),
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
