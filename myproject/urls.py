"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from order.models import Order

urlpatterns = [
    path("sadmin/", admin.site.urls),
    path("tadmin/", include("admin.urls")),
    path("vendor/", include("vendors.urls")),
    path("", include("user.urls")),
    path("shop/", include("store.urls")),
    path("cart/", include("cart.urls")),
    path("orders/", include("order.urls")),
]
