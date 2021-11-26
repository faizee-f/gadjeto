from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from cart.models import Cart, CartItem

from store.models import Variation, VarientColor, product

# Create your views here.

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
    current_user=request.user
    varient=Variation.objects.get(id=product_id)
    if current_user.is_authenticated:
        try:
            cart_item=CartItem.objects.get(varient=varient,user=current_user)
            cart_item.quantity +=1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item=CartItem.objects.create(varient=varient,quantity=1,user=current_user)
            cart_item.save()
        return redirect('cart')
    else:
        try:
            cart=Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

        try:
            cart_item=CartItem.objects.get(varient=varient,cart=cart)
            cart_item.quantity +=1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item=CartItem.objects.create(varient=varient,quantity=1,cart=cart,)
            cart_item.save()
        return redirect('cart')

def remove_cart(request,product_id):
    current_user=request.user
    if current_user.is_authenticated:
        var= get_object_or_404(Variation,id=product_id)
        cart_item=CartItem.objects.get(varient=var,user=current_user)
        if cart_item.quantity>1:
            cart_item.quantity -=1
            cart_item.save()
        else:
            cart_item.delete()
        return redirect('cart')
    else:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        var= get_object_or_404(Variation,id=product_id)
        cart_item=CartItem.objects.get(varient=var,cart=cart)
        if cart_item.quantity>1:
            cart_item.quantity -=1
            cart_item.save()
        else:
            cart_item.delete()
        return redirect('cart')


def delete_cart(request,product_id):
    current_user=request.user
    if current_user.is_authenticated:
        prod= get_object_or_404(Variation,id=product_id)
        cart_item=CartItem.objects.get(varient=prod,user=current_user)
        cart_item.delete()
        return redirect('cart')
    else:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        prod= get_object_or_404(Variation,id=product_id)
        cart_item=CartItem.objects.get(varient=prod,cart=cart)
        cart_item.delete()
        return redirect('cart')


def cart(request,total=0,quantity=0,cart_items=None):
    try:
        tax=0
        grand_total=0
        if request.user.is_authenticated:
            cart_items=CartItem.objects.filter(user=request.user,is_active=True)
        else:
            cart=Cart.objects.get(cart_id=_cart_id(request))
            cart_items=CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            total  += (cart_item.varient.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax= (total*2)/100
        grand_total=total+tax
    except ObjectDoesNotExist:
        pass  

    context={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,
    }  
    return render(request,'cart.html',context)

@login_required(login_url='signin')
def checkout(request,total=0,quantity=0,cart_items=None):
    try:
        tax=0
        grand_total=0
        if request.user.is_authenticated:
            cart_items=CartItem.objects.filter(user=request.user,is_active=True)
        else:
            cart=Cart.objects.get(cart_id=_cart_id(request))
            cart_items=CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            total  += (cart_item.varient.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax= (total*2)/100
        grand_total=total+tax
    except ObjectDoesNotExist:
        pass  

    context={ 
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,
    }  
    return render(request,'checkout.html',context)