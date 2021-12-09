from django import forms
from django.shortcuts import redirect, render
from account.models import Account
from django.contrib import messages, auth
from category.forms import AddCategoryForm
from category.models import category
from django.contrib.auth.decorators import user_passes_test
from offer.form import CouponForm

from offer.models import Coupen, RedeemedCoupen


# Create your views here.


def admin_signin(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    if request.method == "POST":
        print("post")
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(
            email=email, password=password, is_superuser=True)
        if user is not None:
            print("user")
            print("varified")
            auth.login(request, user)
            messages.success(request, 'Login Successful')
            print("login Success")
            return redirect('admin_dashboard')
        else:
            print("Error user")
            messages.error(request, "Invalid credentials")
            return redirect('admin_signin')
    else:
        return render(request, 'admin/admin_login.html')



def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


@user_passes_test(lambda u: u.is_superuser, login_url='forbidden_user')
def customers(request):
    users = Account.objects.all()
    print(users)

    context = {
        'users': users
    }
    return render(request, 'admin/customers.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='forbidden_user')
def vendor_approval(request):
    vendors = Account.objects.filter(is_staff=True)
    print(vendors)
    context = {
        'vendors': vendors
    }
    return render(request, 'admin/vendor_approval.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='forbidden_user')
def approve_vendor(request, vendor_id):
    vendor = Account.objects.get(pk=vendor_id)
    vendor.is_varified = True
    vendor.save()
    return redirect('vendor_approval')


@user_passes_test(lambda u: u.is_superuser, login_url='forbidden_user')
def user_block_unblock(request, customer_id):
    customer = Account.objects.get(pk=customer_id)
    if customer.is_active:
        customer.is_active = False
        messages.success(request, "Done, User Blocked!")
    else:
        customer.is_active = True
        messages.success(request, "Done, User Unblocked!")
    customer.save()

    return redirect('customers')


@user_passes_test(lambda u: u.is_superuser, login_url='forbidden_user')
def reject_vendor(request, vendor_id):
    vendor = Account.objects.get(pk=vendor_id)
    vendor.is_rejected = True
    vendor.save()
    return redirect('vendor_approval')


@user_passes_test(lambda u: u.is_superuser, login_url='forbidden_user')
def admin_signout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out ! ')
    return redirect('admin_signin')


#CATEGORY SELECT

@user_passes_test(lambda u: u.is_superuser, login_url='forbidden_user')
def category_list(request):
    if request.method == "POST":
        print("POSt")
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            messages.success(request, "Category created")
            return redirect('category_list')
        else:
            print("invalid")
            messages.error(request, "Category creation failed")
            return redirect('category_list')
    all_category = category.objects.all()
    print(all_category)
    form = AddCategoryForm()
    context = {
        'all_category': all_category,
        'form': form,
    }
    return render(request, 'admin/category_list.html', context)

def edit_category(request,cat_id):
    item=category.objects.get(id=cat_id)
    if request.method=="POST":
        form=AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    form=AddCategoryForm(instance=item)
    context={'form':form}
    return render(request, 'admin/edit_catitem.html', context)


def delete_category(request,cat_id):
    cat=category.objects.get(id=cat_id)
    cat.delete()
    messages.success(request,'Category deleted')
    return redirect ('category_list')
    
    
# #VARIENT CATEGORY SELECT

# @user_passes_test(lambda u: u.is_superuser, login_url='forbidden_user')
# def varient_category_list(request):
#     if request.method == "POST":
#         print("POSt")
#         form = AddVarientCategoryForm(request.POST)
#         if form.is_valid():
#             print('valid')
#             form.save()
#             messages.success(request, "Sub-category created")
#             return redirect('varient_category_list')
#         else:
#             print("invalid")
#             messages.error(request, "Sub-category creation failed")
#             return redirect('varient_category_list')
#     all_varient_category = VariationCategories.objects.all()
#     print(all_varient_category)
#     form = AddVarientCategoryForm()
#     print(form)
#     context = {
#         'all_varient_category': all_varient_category,
#         'form': form,
#     }
#     return render(request, 'admin/varient_category_list.html', context)

# def edit_varient_category(request,varcat_id):
#     item=VariationCategories.objects.get(id=varcat_id)
#     print("edit")
#     if request.method=="POST":
#         print("submit")
#         form=AddVarientCategoryForm(request.POST)
#         if form.is_valid():
#             print('valid')
#             form.save()
#             return redirect('varient_category_list')
#         else:
#             return redirect('edit_varient_category',varcat_id)
#     form=AddVarientCategoryForm(instance=item)
#     context={'form':form}
#     return render(request, 'admin/edit_subcatitem.html', context)


# def delete_varient_category(request,varcat_id):
#     varcat=VariationCategories.objects.get(id=varcat_id)
#     varcat.delete()
#     return redirect ('varient_category_list')


# #VAREINT ITEM SELECT

# def varient_list(request):
#     if request.method == "POST":
#         print("POSt")
#         form = AddVarientItemForm(request.POST)
#         if form.is_valid():
#             print('valid')
#             form.save()
#             messages.success(request, "Varient Category created")
#             return redirect('varient_list')
#         else:
#             print("invalid")
#             messages.error(request, "Varient Category creation failed")
#             return redirect('varient_list')
#     all_varients = VariationItems.objects.all()
#     print(all_varients)
#     form = AddVarientItemForm()
    
#     context = {
#         'all_varients': all_varients,
#         'form': form,
#     }
#     return render(request,'admin/varient_list.html',context)

# def edit_varient(request,var_id):
#     item=VariationItems.objects.get(id=var_id)
#     print("edit")
#     if request.method=="POST":
#         print("submit")
#         form=AddVarientItemForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('varient_category_list')
#         else:
#             return redirect('edit_varient',var_id)
#     form=AddVarientItemForm(instance=item)
#     context={'form':form}
#     return render(request, 'admin/edit_subcatitem.html', context)


# def delete_varient(request,var_id):
#     var=VariationItems.objects.get(id=var_id)
#     var.delete()
#     return redirect ('varient_category_list')

def coupon_list(request):
    if request.method=="POST":
        form=CouponForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Coupen created ')
            return redirect('coupon_list')
        else:
            messages.error(request,"Failed to add the coupon ")
            return redirect('coupon_list')

    else:
        all_coupons=Coupen.objects.all()
        redeemed_coupen=RedeemedCoupen.objects.all()
        redeemed_coupen_count=redeemed_coupen.count()
        coupen_count=all_coupons.count()
        
        form=CouponForm()
    context={
        'all_coupons':all_coupons,
        'form':form,
        'coupen_count':coupen_count,
        'redeemed_coupen_count':redeemed_coupen_count,
    }
    return render(request,'admin/coupen_list.html',context)

def activate_coupen(request,id):
    coupen=Coupen.objects.get(id=id)
    if coupen.is_active==True:
        coupen.is_active=False
        coupen.save()
        messages.success(request,'Coupen disabled')
    else:
        coupen.is_active=True
        coupen.save()
        messages.success(request,'Coupen enabled')
    return redirect('coupon_list')


def delete_coupen(request,id):
    Coupen.objects.get(id=id).delete()
    messages.success(request,'Coupen deleted successfully ')
    return redirect('coupon_list')

def edit_coupon(request,id):
    edit=Coupen.objects.get(id=id)
    if request.method=='POST':
        form=CouponForm(request.POST,instance=edit)
        if form.is_valid():
            form.save()
            return redirect('coupon_list')
        else:
            print(form.errors)
    else:
        edit=Coupen.objects.get(id=id)
        form=CouponForm(instance=edit)
    context={
        'form':form,
    }
    return render(request,'admin/edit_coupon.html',context)