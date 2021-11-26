
from django.contrib.auth.models import User
from django.db.models.indexes import Index
from django.shortcuts import redirect, render
from account.forms import VendorRegistrationForm
from django.contrib import messages, auth
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from store.forms import AddProductForm
from store.models import product
from vendors.forms import RegisterVendor
from vendors.models import Vendors
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied


# from django.contrib.auth.decorators import user_passes_test

# def email_check(user):
#     return user.email.endswith('@example.com')

# @user_passes_test(email_check)
# def my_view(request):
#     ...

# Create your views here.
@staff_member_required(login_url='forbidden_user')
def vendor_home(request):
    return render(request,'vendor/index.html')



def vendor_signup(request):
    if request.user.is_authenticated:
        return redirect('vendor_home')
    if request.method=='POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            password = form.cleaned_data['password']
            print("Processing")
            user = Account.objects.create_vendor(
                first_name=first_name,
                mobile=mobile,
                email=email,
                password=password,
            )
            user.save()
            print("saved")
            messages.success(request, 'Registered Sucessfully')
            return redirect('vendor_signup')

    else:
        form = VendorRegistrationForm()
    context = {'form': form, } 
    return render(request,'vendor/register.html',context)

def vendor_signin(request):
    if request.user.is_authenticated:
        return redirect('vendor_home')
    if request.method=="POST":
        print("post")
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password,is_staff=True)
        if user is not None:
            print("user")
            if user.is_varified==True:
                print("varified")
                auth.login(request,user)
                messages.success(request,'Login Successful')
                print("login Success")
                return redirect('vendor_home')
            else:
                print("Error varification")
                messages.info(request,"Account is not varified")
                return redirect('vendor_signin')
        else:
            print("Error user")
            messages.error(request,"Invalid credentials")
            return redirect('vendor_signin')
    else:
        return render(request,'vendor/login.html')

@staff_member_required(login_url='forbidden_user')
def vendor_signout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out ! ')
    return redirect('vendor_signin')


@staff_member_required(login_url='forbidden_user')
def vendor_profile(request):
    if request.method=="POST":
        curr_user=request.user
        form=RegisterVendor(request.POST)
        print("valid")
        if form.is_valid():
            var=form.save(commit=False)
            var.vendor_id=curr_user 
            var.save()
            print("saved")
        return redirect('vendor_profile')
    else:
        curr_user=request.user
        print(curr_user)
        print(type(curr_user))
        data=Vendors.objects.get(vendor_id=curr_user)
        form=RegisterVendor(instance=data)
        
        context={'form':form}
    
    return render(request,'vendor/profile.html',context)



def add_product(request):
    curr_user=request.user
    print(curr_user)
    vendor=Vendors.objects.get(vendor_id=curr_user.id)
    print(vendor)
    if request.method=="POST":
        form=AddProductForm(request.POST)
        if form.is_valid():
            prod=form.save(commit=False)
            prod.vendor=vendor
            if len(request.FILES)!=0:
                prod.image1=request.FILES['image1']
            prod.save()
            messages.success(request,"product Added Successfully")
            return redirect(add_product)
        else:
            messages.info(request,'Something went wrong')
            return redirect(add_product)
    form=AddProductForm()
    context={
        'form':form
    }
    return render(request,'vendor/add_product.html',context)

def view_product(request):
    curr_user=request.user
    print(curr_user)
    try:
        vendor=Vendors.objects.get(vendor_id=curr_user.id)
    except ObjectDoesNotExist:
        messages.warning(request,"Update your profile First")
        return redirect(vendor_home)
    print(vendor)
    prods=product.objects.filter(vendor=vendor)
    print(prods)
    context={
        'prods':prods
    }
    return render(request,'vendor/product.html',context)