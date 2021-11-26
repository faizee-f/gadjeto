from django.core import paginator
from django.db.models import Q
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from category.models import category
from store.models import Variation, product
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def shop(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(category, slug=category_slug)
        products = product.objects.all().filter(category=categories, is_available=True)
        varients=Variation.objects.all().filter(product=products,is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = varients.count()
    else:
        varients=Variation.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(varients, 3)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)

        product_count = varients.count()

    context = {
        'products': paged_product,
        'product_count': product_count
    }
    return render(request, 'category.html', context)


def product_detail(request, category_slug, product_slug,varient_slug):
    try:
        # single_product = product.objects.get(
        #     category__slug=category_slug, slug=product_slug)
        single_varient=Variation.objects.get(
            product__slug=product_slug,slug=varient_slug
        )
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(
            request), varient=single_varient).exists()
        print(in_cart)
    except Exception as e:
        raise e
    print(single_varient)
    varients=Variation.objects.filter(product=single_varient.product.id)
    print(varients)
    context = {'single_varient': single_varient, 'in_cart': in_cart, 'varients':varients }
    return render(request, 'product.html', context)


def search(request):

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count=products.count()
    context = {
        'products': products,
        'product_count':product_count,
    }
    return render(request, 'category.html', context)
