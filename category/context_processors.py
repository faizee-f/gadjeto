from vendors.models import Vendors
from .models import category


def menu_links(request):
    links= category.objects.all()
    return dict(links=links)

def brand_link(request):
    brand_link=Vendors.objects.all()
    return dict(brand_link=brand_link)
