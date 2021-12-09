from typing_extensions import OrderedDict
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from cart.models import CartItem
from offer.models import Coupen, RedeemedCoupen
from order.forms import OrderForm
from order.models import Order, OrderProduct, Payment
from store.models import Variation
import datetime
import json
from django.urls import reverse
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

# Create your views here.

@never_cache
def payments(request):
    curr_user = request.user
    body = json.loads(request.body)
    print(body)
    iorder = Order.objects.get(
        user=curr_user, is_ordered=False, order_number=body['orderID'])
    print(iorder)
    print(iorder.id)

    # save payment informations
    payment = Payment(
        user=curr_user,
        payment_id=body['transID'],
        payment_method=body['payment_method'],
        amount_paid=iorder.order_total,
        status=body['status'],
    )
    payment.save()
    iorder.payment = payment
    iorder.is_ordered = True
    iorder.save()

    # move cart items to order product table

    if 'quick_buy' in  request.session:
        id=request.session['quick_buy']
        varient=Variation.objects.get(id=id)


        orderproduct = OrderProduct()
        orderproduct.order_id = iorder.id
        orderproduct.payment = payment
        orderproduct.user_id = curr_user.id
        orderproduct.vendor = varient.product.vendor
        orderproduct.products_id = varient.product.id
        orderproduct.variation_id = varient.id
        orderproduct.quantity = 1
        if varient.offer_price():
            off_price = Variation.offer_price(varient)
            price = int(off_price['new_price'])
            orderproduct.price = price
        else:
            orderproduct.price = varient.price
        orderproduct.ordered = True
        orderproduct.save()

    # reduce the stock

        varient = Variation.objects.get(id=varient.id)
        varient.stock -= 1
        varient.save()

    else:
        cart_items = CartItem.objects.filter(user=curr_user)

        for item in cart_items:
            orderproduct = OrderProduct()
            orderproduct.order_id = iorder.id
            orderproduct.payment = payment
            orderproduct.user_id = curr_user.id
            orderproduct.vendor = item.varient.product.vendor
            orderproduct.products_id = item.varient.product.id
            orderproduct.variation_id = item.varient.id
            orderproduct.quantity = item.quantity
            if item.varient.offer_price():
                off_price = Variation.offer_price(item.varient)
                price = int(off_price['new_price'])
                orderproduct.price = price
            else:
                orderproduct.price = item.varient.price
            orderproduct.ordered = True
            orderproduct.save()

        # reduce the stock

            varient = Variation.objects.get(id=item.varient_id)
            print(varient)
            print(varient.stock)
            varient.stock -= item.quantity
            varient.save()

        # clear the cart
        CartItem.objects.filter(user=request.user).delete()

    #check the coupen code
    #store coupen data
    check =redeem_coupen(request)

    # send transaction successfull
    data = {
        'order_number': iorder.order_number,
        'trans_id': payment.payment_id,

    }
    return JsonResponse(data)



def place_order(request, total=0, quantity=0):
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()

    if not 'quick_buy' in request.session:
        if cart_count <= 0:
            return redirect('shop')

    grand_total = 0
    tax = 0

    if 'quick_buy' in request.session:
        varient_id=request.session['quick_buy']
        cart_items=Variation.objects.get(id=varient_id)
        check=True
        if cart_items.offer_price():
            off_price=Variation.offer_price(cart_items)
            total  = (off_price['new_price'])
            print(total)
        else:
            total  = (cart_items.price )
        quantity = 1
    else:
        check=False
        for cart_item in cart_items:
            if cart_item.varient.offer_price():
                off_price = Variation.offer_price(cart_item.varient)
                total += int(off_price['new_price'] * cart_item.quantity)
                print(total)
            else:
                total += int(cart_item.varient.price * cart_item.quantity)
            quantity += int(cart_item.quantity)
    tax = (2*total)/100
    grand_total = total+tax
    if 'total_after_discount' in request.session:
        grand_total = request.session['total_after_discount']
    grand_total = int(grand_total)
    discount = None
    if 'discount' in request.session:
        discount = request.session['discount']
    coupen_code=None
    if 'coupen_code' in request.session:
        coupen_code = request.session['coupen_code']
    request.session['total'] = grand_total
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            print("Valid Order Form")
            # order creation
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address1 = form.cleaned_data['address1']
            data.address2 = form.cleaned_data['address2']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.pincode = form.cleaned_data['pincode']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            yr = int(datetime.date.today().strftime('%Y'))
            mt = int(datetime.date.today().strftime('%m'))
            dt = int(datetime.date.today().strftime('%d'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")

            payment_type = request.POST['payment']
            
            

            currency = 'INR'
            amount = grand_total*100
            request.session['razorpay_amount'] = amount
            # Create a Razorpay Order
            razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                               currency=currency,
                                                               payment_capture='0'))
            if payment_type=="razorpay":
                order_number=razorpay_order['id']
                data.order_number = razorpay_order['id']
                data.save()
            else:
                order_number = current_date+str(data.id)
                data.order_number =order_number
                request.session['order_number']=order_number
                data.save()
            
            # order id of newly created order.
            razorpay_order_id = razorpay_order['id']
            callback_url = 'paymenthandler/'
            # saving the address
            

            order = Order.objects.get(
                user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
                'razorpay_order_id': razorpay_order_id,
                'razorpay_merchant_key': settings.RAZOR_KEY_ID,
                'razorpay_amount': amount,
                'currency': currency,
                'callback_url': callback_url,
                'discount': discount,
                'coupen_code': coupen_code,
                'payment_type': payment_type,
                'check':check,
            }
            return render(request, 'payment.html', context)
        else:
            return redirect('checkout')


@csrf_exempt 
@never_cache
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is None:
                amount = request.session['razorpay_amount']
                try:
                    razorpay_client.payment.capture(payment_id, amount)
                    messages.success(request, "Payment Successfull")
                    ################
                    curr_user = request.user
                    iorder = Order.objects.get(
                        user=curr_user, is_ordered=False, order_number=razorpay_order_id)
                    print(iorder)
                    print(iorder.id)

                    # save payment informations
                    payment = Payment(
                        user=curr_user,
                        payment_id=payment_id,
                        payment_method="RazorPay",
                        amount_paid=iorder.order_total,
                        status="Paid",
                    )
                    payment.save()
                    iorder.payment = payment
                    iorder.is_ordered = True
                    iorder.save()

                    # move cart items to order product table
                    if 'quick_buy' in  request.session:
                        id=request.session['quick_buy']
                        varient=Variation.objects.get(id=id)


                        orderproduct = OrderProduct()
                        orderproduct.order_id = iorder.id
                        orderproduct.payment = payment
                        orderproduct.user_id = curr_user.id
                        orderproduct.vendor = varient.product.vendor
                        orderproduct.products_id = varient.product.id
                        orderproduct.variation_id = varient.id
                        orderproduct.quantity = 1
                        if varient.offer_price():
                            off_price = Variation.offer_price(varient)
                            price = int(off_price['new_price'])
                            orderproduct.price = price
                        else:
                            orderproduct.price = varient.price
                        orderproduct.ordered = True
                        orderproduct.save()

                    # reduce the stock

                        varient = Variation.objects.get(id=varient.id)
                        varient.stock -= 1
                        varient.save()

                    else:

                        cart_items = CartItem.objects.filter(user=curr_user)

                        for item in cart_items:
                            orderproduct = OrderProduct()
                            orderproduct.order_id = iorder.id
                            orderproduct.payment = payment
                            orderproduct.user_id = curr_user.id
                            orderproduct.vendor = item.varient.product.vendor
                            orderproduct.products_id = item.varient.product.id
                            orderproduct.variation_id = item.varient.id
                            orderproduct.quantity = item.quantity
                            if item.varient.offer_price():
                                off_price = Variation.offer_price(item.varient)
                                price = int(off_price['new_price'])
                                orderproduct.price = price
                            else:
                                orderproduct.price = item.varient.price
                            orderproduct.ordered = True
                            orderproduct.save()

                        # reduce the stock

                            varient = Variation.objects.get(id=item.varient_id)
                            print(varient)
                            print(varient.stock)
                            varient.stock -= item.quantity
                            varient.save()

                        # clear the cart
                        CartItem.objects.filter(user=request.user).delete()
                    # send transaction successfull
                    data = {
                        'order_number': iorder.order_number,
                        'trans_id': payment.payment_id,

                    }
                    param="order_number=" + iorder.order_number + "&payment_id=" + payment.payment_id
                    ################
                    # capture the payemt
                    messages.success(request, "Payment Success")
                    print("hello")


                    #save coupen offer
                    #store coupen data

                    check =redeem_coupen(request)
                    print(check)


                    redirect_url = reverse('order_complete')
                    return redirect(f'{redirect_url}?{param}')
                    # render success page on successful caputre of payment
                except Exception as e:
                    print(e)
                    messages.error(request, "Payment Failed")
                    # if there is an error while capturing payment.
                    return redirect('checkout')
            else:

                return redirect('checkout')
                # if signature verification fails.

        except:
            return redirect('checkout')
            # if we don't find the required parameters in POST data
    else:
       # if other than POST request is made.
        return redirect('checkout')



@never_cache
def cash_on_delivery(request):
    curr_user = request.user
    order_number=request.session['order_number']
    iorder = Order.objects.get(
        user=curr_user, is_ordered=False, order_number=order_number)
    print(iorder)
    # save payment informations
    payment = Payment(
        user=curr_user,
        payment_id=order_number,
        payment_method="Cash on Delivery",
        amount_paid=iorder.order_total,
        status="Paid",
    )
    payment.save()
    iorder.payment = payment
    iorder.is_ordered = True
    iorder.save()

    # move cart items to order product table

    if 'quick_buy' in  request.session:
        id=request.session['quick_buy']
        varient=Variation.objects.get(id=id)


        orderproduct = OrderProduct()
        orderproduct.order_id = iorder.id
        orderproduct.payment = payment
        orderproduct.user_id = curr_user.id
        orderproduct.vendor = varient.product.vendor
        orderproduct.products_id = varient.product.id
        orderproduct.variation_id = varient.id
        orderproduct.quantity = 1
        if varient.offer_price():
            off_price = Variation.offer_price(varient)
            price = int(off_price['new_price'])
            orderproduct.price = price
        else:
            orderproduct.price = varient.price
        orderproduct.ordered = True
        orderproduct.save()

    # reduce the stock

        varient = Variation.objects.get(id=varient.id)
        varient.stock -= 1
        varient.save()

    else:
        cart_items = CartItem.objects.filter(user=curr_user)

        for item in cart_items:
            orderproduct = OrderProduct()
            orderproduct.order_id = iorder.id
            orderproduct.payment = payment
            orderproduct.user_id = curr_user.id
            orderproduct.vendor = item.varient.product.vendor
            orderproduct.products_id = item.varient.product.id
            orderproduct.variation_id = item.varient.id
            orderproduct.quantity = item.quantity
            if item.varient.offer_price():
                off_price = Variation.offer_price(item.varient)
                price = int(off_price['new_price'])
                orderproduct.price = price
            else:
                orderproduct.price = item.varient.price
            orderproduct.ordered = True
            orderproduct.save()

        # reduce the stock

            varient = Variation.objects.get(id=item.varient_id)
            print(varient)
            print(varient.stock)
            varient.stock -= item.quantity
            varient.save()

        # clear the cart
        CartItem.objects.filter(user=request.user).delete()
    
    #store coupen data

    check =redeem_coupen(request)
    print(check)
    
    # send transaction successfull


    data = {
        'order_number': iorder.order_number,
        'trans_id': payment.payment_id,

    }
    param="order_number=" + iorder.order_number + "&payment_id=" + payment.payment_id
    
    messages.success(request, "Payment Success")
    if 'order_number' in request.session:
        del request.session['order_number']

    redirect_url = reverse('order_complete')
    return redirect(f'{redirect_url}?{param}')

def redeem_coupen(request):
    
    if 'discount' in request.session:
        coupen_code = request.session['coupen_code']
        curr_user=request.user
        coupen=Coupen.objects.get(coupen_code=coupen_code)
        coupen.coupen_count -=1
        coupen.save()
        redeem=RedeemedCoupen()
        redeem.user=curr_user
        redeem.coupen=coupen
        redeem.save()

        del request.session['discount']
        del request.session['total_after_discount']
        del request.session['coupen_code']
        return True
    else:
        return False


@never_cache
def order_complete(request):
    order_number = request.GET.get('order_number')
    trans_id = request.GET.get('payment_id')
    try:
        order = Order.objects.get(order_number=order_number, is_ordered=True)
        order_products = OrderProduct.objects.filter(order_id=order.id)
        sub_total = 0

        for i in order_products:
            sub_total += i.price * i.quantity

        context = {
            'order': order,
            'sub_total': sub_total,
            'order_products': order_products}
        return render(request, 'order-complete.html', context)
    except(ObjectDoesNotExist):
        return redirect('home')

