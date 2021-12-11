from django.core import paginator
from django.contrib import messages
from django.db.models import Q
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from category.models import category
from offer.models import VariationOffer
from order.models import OrderProduct
from store.forms import ReviewForm
from store.models import ReviewRating, Variation, product
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

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
        varients=Variation.objects.all().filter(is_available=True)
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

    try:
        ordered=OrderProduct.objects.filter(user=request.user,variation=single_varient).exists()
    except:
        ordered=None
    print(single_varient)
    print(ordered)
    varients=Variation.objects.filter(product=single_varient.product.id)
    print(varients)
    reviews=ReviewRating.objects.filter(varient=single_varient,status=True)
    review_count=reviews.count()
    avg_total=0
    average=0
    for i in reviews:
        avg_total += i.rating

    try:
        average=(avg_total/review_count)*20
    except:
        pass
    print(reviews)
    context = {
        'single_varient': single_varient, 
        'in_cart': in_cart, 
        'varients':varients,
        'reviews':reviews,
        'review_count':review_count,
        'ordered':ordered,
        'average':average,
    }
    return render(request, 'product.html', context)


def search(request):

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Variation.objects.order_by('-created_at').filter(
                Q(product__description__icontains=keyword) | Q(product__product_name__icontains=keyword) | Q(varient_name__icontains=keyword) | Q(product__vendor__brand_name__icontains=keyword) )
            product_count=products.count()
    context = {
        'products': products,
        'product_count':product_count,
    }
    return render(request, 'category.html', context)


def submit_review(request,varient_id):
    url=request.META.get('HTTP_REFERER')
    varient=Variation.objects.get(id=varient_id)
    if request.method=="POST":
        try:
            review=ReviewRating.objects.get(user__id=request.user.id,varient__id=varient_id)
            form=ReviewForm(request.POST,instance=review)
            form.save()
            messages.success(request,"Thank You, Your review has been updated")
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form=ReviewForm(request.POST)
            if form.is_valid():
                reviews=ReviewRating()
                reviews.subject=form.cleaned_data['subject']
                reviews.rating=form.cleaned_data['rating']
                reviews.review=form.cleaned_data['review']
                reviews.user=request.user
                reviews.varient_id=varient_id
                reviews.ip=request.META.get('REMOTE_ADDR')
                reviews.save()
                messages.success(request,'Thank You, Your review has been submitted')
                return redirect(url)
    return redirect(url)


def quick_buy(request,id):
    varient=Variation.objects.get(id=id)
    if 'quick_buy' in request.session:
        del request.session['quick_buy']
    request.session['quick_buy']=varient.id
    return redirect('checkout')