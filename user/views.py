
from django.shortcuts import redirect, render
from account.forms import RegistrationForm
from account.models import Account
from cart.models import Cart, CartItem
from category.models import category
from order.models import  OrderProduct
from store.models import Variation
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from account.otp import sendOTP, varifyOTP
from cart.views import _cart_id
from user.models import Address, Profile

import requests

from user.forms import AddAdddressForm, UserProfileForm
# Create your views here.


@login_required(login_url='signin')
def dashboard(request):

    orders=OrderProduct.objects.filter(user=request.user).order_by('updated_at')
    total_orders=orders.count()
    usr_profile=Profile.objects.get(user=request.user.id)
    context={
        'total_orders':total_orders,
        'usr_profile':usr_profile
    }
    return render(request,'user_dashboard/dashboard.html',context)


@login_required(login_url='signin')
def user_order(request):
    orders=OrderProduct.objects.filter(user=request.user).order_by('-created_at')
    context={
        'orders':orders,
    }
    return render(request,'user_dashboard/orderes.html',context)


@login_required(login_url='signin')
def user_address(request):
    if request.method=="POST":
        form=AddAdddressForm(request.POST)
        if form.is_valid():
            address=form.save(commit=False)
            address.user=request.user
            address.save()
            
            messages.success(request,"Address added Successfully")
            return redirect('user_address')
    address=Address.objects.filter(user=request.user)
    form=AddAdddressForm()
    context={
        'form':form,
        'address':address,
    }
    return render(request,'user_dashboard/address.html',context)

@login_required(login_url='signin')
def edit_address(request,id):
    addr=Address.objects.get(id=id)
    if request.method=="POST":
        form=AddAdddressForm(request.POST)
        if form.is_valid():
            address=form.save(commit=False)
            address.user=request.user
            address.id=id
            address.save()
            messages.success(request,"Address updated Successfully")
            return redirect('user_address')
    check=True
    form=AddAdddressForm(instance=addr)
    context={
        'form':form,
        'check':check,
    }
    return render(request,'user_dashboard/address.html',context)

@login_required(login_url='signin')
def delete_address(request,id):
    address=Address.objects.get(id=id)
    address.delete()
    messages.success(request,"Address deleted Successfully")
    return redirect('user_address')


@login_required(login_url='signin')
def user_profile(request):
    usr_profile=Profile.objects.get(user=request.user.id)
    form=UserProfileForm(instance=usr_profile)
    if request.method =="POST":
        form=UserProfileForm(request.POST,request.FILES,instance=usr_profile)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile updated Successfully")
            return redirect('user_profile')
        else:
            print(form.errors)
   
    context={
        'form':form,
        'usr_profile':usr_profile,
    }
    return render(request,'user_dashboard/profile.html',context)


    

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

@login_required(login_url='signin')
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
    # try:
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
            profile=Profile()
            profile.first_name=first_name
            profile.last_name=last_name
            profile.user=user
            profile.gender=gender
            profile.phone=mobile_number
            profile.email=email
            profile.profile_picture='user/profile/profile.png'
            profile.save()
            user.save()
            return redirect("signin")
        else:
            messages.info(request, "Invalid OTP")
            return redirect('register_otp')
    # except:
    #     messages.info(request, "Registration Failed, Please Register Again")
    #     return redirect('register')
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

@login_required(login_url='signin')
def cancel_order(request,id):
    item=OrderProduct.objects.get(id=id)
    item.status='Cancelled'
    item.save()
    return redirect('user_order')

@login_required(login_url='signin')
def change_password(request):
    if request.method=="POST":
        current_password=request.POST['current_password']
        new_password=request.POST['new_password']
        confirm_password=request.POST['confirm_password']

        user=Account.objects.get(email__exact=request.user.email)
        
        if new_password==confirm_password:
            success=user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                messages.success(request,"Password changed Successfully")
                return redirect('change_password')
            else:
                messages.error(request,"Wrong password, Try again")
                return redirect('change_password')
        else:
            messages.error(request,"Password Doesn't match !")
            return redirect('change_password')
        
        
    return render(request,'user_dashboard/reset_password.html')
