
from django.db.models import indexes
from django.db.models.indexes import Index
from django.shortcuts import redirect, render
from account.forms import RegistrationForm
from account.models import Account
from cart.models import Cart, CartItem
from category.models import category
from store.models import Variation, product
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from account.otp import sendOTP, varifyOTP
from cart.views import _cart_id
import requests
# Create your views here.


def home(request):
    products = Variation.objects.all().filter(is_available=True)
    print(products)
    categories = category.objects.all()
    print(category)
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        print("login POST")
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                print(cart)
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    print("cart exist")
                    cart_item = CartItem.objects.filter(cart=cart)
                    print(cart_item)
                    user_cart=CartItem.objects.filter(user=user)
                    if user_cart:
                        for item in cart_item:
                            counter=0
                            for x in user_cart:
                                if x.varient==item.varient:
                                    x.quantity+=item.quantity
                                    x.save()
                                    counter=1
                            if counter!=1:
                                item.user=user
                                item.save()
                    else:
                        for item in cart_item:
                            item.user=user
                            item.save()



                #     product_variation = []
                #     for item in cart_item:
                #         variation = item.varient.all()
                #         product_variation.append(list(variation))

                #     print(product_variation)
                #     cart_item = CartItem.objects.filter(user=user)
                #     print("cart 1 exist")
                #     ex_var_list = []
                #     id = []
                #     for item in cart_item:
                #         existing_variation = item.varient.all()
                #         ex_var_list.append(list(existing_variation))
                #         id.append(item.id)
                #     print("cart 1 exist")
                #     for pr in product_variation:
                #         if pr in ex_var_list:
                #             index = ex_var_list.index(pr)
                #             item_id = id[index]
                #             item = CartItem.objects.get(id=item_id)
                #             item.quantity += 1
                #             item.user = user
                #             item.save()
                #         else:
                #             cart_item = CartItem.objects.filter(cart=cart)
                #             for item in cart_item:
                #                 item.user = user
                #                 item.save()
            except:
                pass
            auth.login(request, user)
            messages.success(request, "Login Successful")
            print("Login Success")
            url=request.META.get('HTTP_REFERER')
            try:
                query=requests.utils.urlparse(url).query
                params=dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage=params['next']
                    return redirect(nextPage)
            except:
                return redirect('home')
                
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('signin')

    return render(request, 'login.html')


def forgot_password(request):
    messages.forgot(request, "Reset Password")
    messages.msg(request, "Enter your mobile Number !")
    return redirect(signin_otp)


def signin_otp(request):
    if 'password' in request.session:
        del request.session['password']
        request.session.modified = True
    global mobile_number
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        mobile_number = request.POST['phone']
        try:
            if Account.objects.get(mobile=mobile_number):
                request.session['otpnumber'] = mobile_number
                sendOTP(mobile_number)
                print(mobile_number)
                messages.success(request, "OTP send to the number")
                return redirect('otp_validation')
        except Account.DoesNotExist:
            messages.error(request, "User is not registered")
            return redirect('signin_otp')
    return render(request, 'otplogin.html')


def resend_otp(request):
    otpnumber = request.session['otpnumber']
    sendOTP(otpnumber)
    messages.info(request, 'OTP has send')
    return redirect('otp_validation')


def register(request):
    global mobile_number
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            mobile_number = form.cleaned_data['mobile']
            password = form.cleaned_data['password']

            request.session['first_name'] = first_name
            request.session['last_name'] = last_name
            request.session['email'] = email
            request.session['gender'] = gender
            request.session['mobile_number'] = mobile_number
            request.session['password'] = password
            sendOTP(mobile_number)
            print(mobile_number)

            return redirect('register_otp')
    else:
        form = RegistrationForm()
    context = {'form': form, }
    return render(request, 'register.html', context)


def register_otp(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        check_otp = request.POST['otpval']
        print(check_otp)
        mobile_number = request.session['mobile_number']
        check = varifyOTP(mobile_number, check_otp)
        if check:
            messages.success(request, "Registered Successfully ! ")
            first_name = request.session['first_name']
            last_name = request.session['last_name']
            email = request.session['email']
            gender = request.session['gender']
            mobile_number = request.session['mobile_number']
            password = request.session['password']
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, mobile=mobile_number, password=password)
            user.gender = gender
            user.save()
            return redirect("signin")
        else:
            messages.info(request, "Invalid OTP")
            return redirect('register_otp')
    return render(request, 'otp_validation.html')


def otp_validation(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        check_otp = request.POST['otpval']
        check = varifyOTP(mobile_number, check_otp)
        if check:
            messages.success(request, 'OTP varified')
            print("OTP varified")
            user = Account.objects.get(mobile=mobile_number)
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid OTP')
            return redirect('otp_validation')
    return render(request, 'otp_validation.html')


@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out ! ')
    return redirect('home')


def forbidden_user(request):
    return render(request, 'forbidden.html')
