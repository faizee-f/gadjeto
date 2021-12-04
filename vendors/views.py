
import json
from django.contrib.auth.models import User
from django.db.models.indexes import Index
from django.db.models.query_utils import select_related_descend
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from account.forms import VendorRegistrationForm
from django.contrib import messages, auth
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from offer.form import ProductOfferForm, VariationOfferForm, VendorOfferForm
from offer.models import ProductOffer, VariationOffer, VendorOffer
from store.forms import AddProductForm, AddVariationForm
from store.models import Variation, product
from order.models import Order, OrderProduct
from vendors.forms import RegisterVendor
from vendors.models import Vendors
from django.http import HttpResponseRedirect
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
    return render(request, 'vendor/dashboard.html')


def vendor_signup(request):
    if request.user.is_authenticated:
        return redirect('vendor_home')
    if request.method == 'POST':
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
    return render(request, 'vendor/register.html', context)


def vendor_signin(request):
    if request.user.is_authenticated:
        return redirect('vendor_home')
    if request.method == "POST":
        print("post")
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password, is_staff=True)
        if user is not None:
            print("user")
            if user.is_varified == True:
                print("varified")
                auth.login(request, user)
                messages.success(request, 'Login Successful')
                print("login Success")
                return redirect('vendor_home')
            else:
                print("Error varification")
                messages.info(request, "Account is not varified")
                return redirect('vendor_signin')
        else:
            print("Error user")
            messages.error(request, "Invalid credentials")
            return redirect('vendor_signin')
    else:
        return render(request, 'vendor/login.html')


@staff_member_required(login_url='forbidden_user')
def vendor_signout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out ! ')
    return redirect('vendor_signin')


@staff_member_required(login_url='forbidden_user')
def vendor_profile(request):
    if request.method == "POST":
        curr_user = request.user
        form = RegisterVendor(request.POST)
        print("valid")
        if form.is_valid():
            var = form.save(commit=False)
            var.vendor_id = curr_user
            var.save()
            print("saved")
        return redirect('vendor_profile')
    else:
        try:
            curr_user = request.user
            print(curr_user)
            print(type(curr_user))
            data = Vendors.objects.get(vendor_id=curr_user)
            form = RegisterVendor(instance=data)
        except:
            form = RegisterVendor()
        context = {'form': form}

    return render(request, 'vendor/profile.html', context)


def add_product(request):
    curr_user = request.user
    print(curr_user)
    vendor = Vendors.objects.get(vendor_id=curr_user.id)
    print(vendor)
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.vendor = vendor
            if len(request.FILES) != 0:
                prod.image1 = request.FILES['image1']
            prod.save()
            messages.success(request, "product Added Successfully")
            return redirect(add_product)
        else:
            print(form.errors)
            messages.info(request, 'Something went wrong')
            return redirect(add_product)
    form = AddProductForm()
    context = {
        'form': form
    }
    return render(request, 'vendor/add_product.html', context)


def view_product(request):
    curr_user = request.user
    print(curr_user)
    try:
        vendor = Vendors.objects.get(vendor_id=curr_user.id)
    except ObjectDoesNotExist:
        messages.warning(request, "Update your profile First")
        return redirect(vendor_home)
    print(vendor)
    prods = product.objects.filter(vendor=vendor)
    print(prods)
    context = {
        'prods': prods
    }
    return render(request, 'vendor/product.html', context)


def edit_product(request, id):
    curr_user = request.user
    try:
        vendor = Vendors.objects.get(vendor_id=curr_user.id)
    except ObjectDoesNotExist:
        messages.warning(request, "Update your profile First")
        return redirect(vendor_home)
    edit_product = product.objects.get(id=id)
    form = AddProductForm(instance=edit_product)
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES,
                              instance=edit_product)
        if form.is_valid():
            form.save()
            messages.success(request, "product updated Successfully")
            return redirect('view_product')
        else:
            messages.info(request, 'Something went wrong')
            return redirect('add_product')

    context = {
        'form': form,
        'check': True
    }
    return render(request, 'vendor/add_product.html', context)


def delete_product(request, id):
    product.objects.get(id=id).delete()
    messages.success(request, "Product has been deleted ")
    return redirect('view_product')


def activate_product(request, id):
    selected_product = product.objects.get(pk=id)
    if selected_product.is_available:
        selected_product.is_available = False
        messages.success(request, "Done, Product is not available now !")
    else:
        selected_product.is_available = True
        messages.success(request, "Done, Product is available !")
    selected_product.save()

    return redirect('view_product')


def view_varient(request, id):
    curr_user = request.user
    selected_product = product.objects.get(id=id)
    print(curr_user)
    try:
        vendor = Vendors.objects.get(vendor_id=curr_user.id)
    except ObjectDoesNotExist:
        messages.warning(request, "Update your profile First")
        return redirect(vendor_home)
    print(vendor)
    varients = Variation.objects.filter(product=id)
    form = AddVariationForm()
    print(varients)
    context = {
        'varients': varients,
        'selected_product': selected_product,
        'form': form
    }
    return render(request, 'vendor/varients.html', context)


def varient_list(request):
    varients = Variation.objects.all().order_by('created_at')
    context = {
        'varients': varients,
    }
    return render(request, 'vendor/varient-list.html', context)


def add_varient(request, id=None):
    selected_product = product.objects.get(id=id)
    if request.method == "POST":
        form = AddVariationForm(request.POST, request.FILES)
        data = {}
        if form.is_valid():
            var = form.save(commit=False)
            var.product = selected_product
            if len(request.FILES) != 0:
                var.image = request.FILES['image']
            var.save()
            messages.success(request, 'Variation saved Successfully')
            return redirect('varient_list')
        else:
            print(form.errors)
            messages.info(request, 'Something went wrong , Try again ')
            return redirect('varient_list')
    form = AddVariationForm()
    context = {
        'form': form
    }
    return render(request, 'vendor/add_varient.html', context)


def edit_varient(request, id=None):
    curr_user = request.user
    try:
        vendor = Vendors.objects.get(vendor_id=curr_user.id)
    except ObjectDoesNotExist:
        messages.warning(request, "Update your profile First")
        return redirect(vendor_home)
    edit_variation = Variation.objects.get(id=id)
    form = AddVariationForm(instance=edit_variation)
    if request.method == "POST":
        form = AddVariationForm(
            request.POST, request.FILES, instance=edit_variation)
        if form.is_valid():
            form.save()
            messages.success(request, "variation updated Successfully")
            return redirect('varient_list')
        else:
            messages.info(request, 'Something went wrong')
            return redirect('edit_varient')

    context = {
        'form': form,
        'check': True
    }
    return render(request, 'vendor/add_varient.html', context)


def activate_varient(request, id):
    selected_varient = Variation.objects.get(pk=id)
    if selected_varient.is_available:
        selected_varient.is_available = False
        messages.success(request, "Done, Product is not available now !")
    else:
        selected_varient.is_available = True
        messages.success(request, "Done, Product is available !")
    selected_varient.save()

    return redirect('varient_list')


def delete_varient(request, id):
    Variation.objects.get(id=id).delete()
    messages.success(request, "Variation has been deleted ")
    return redirect('varient_list')


def view_order(request):
    try:
        vendor = Vendors.objects.get(vendor_id=request.user.id)
        print(vendor)
    except ObjectDoesNotExist:
        messages.warning(request, "Update your profile First")
        return redirect(vendor_home)
    ordered_products = OrderProduct.objects.filter(vendor=vendor)
    print(ordered_products)
    context = {
        'ordered_products': ordered_products
    }
    return render(request, 'vendor/order.html', context)


def view_order_detail(request, order_id):

    ordered_product = OrderProduct.objects.get(id=order_id)
    print(ordered_product)
    context = {
        'ordered_product': ordered_product
    }

    return render(request, 'vendor/order-detail.html', context)


def view_offers(request):
    vendor = Vendors.objects.get(vendor_id=request.user.id)
    try:
        brand_offer = VendorOffer.objects.get(vendor_name=vendor)
    except VendorOffer.DoesNotExist:
        brand_offer = None

    product_offers = ProductOffer.objects.filter(product_name__vendor=vendor)
    print(product_offers)
    varient_offers = VariationOffer.objects.filter(
        variation_name__product__vendor=vendor)
    print(varient_offers)
    total_offers = product_offers.count()+varient_offers.count()
    context = {
        'brand_offer': brand_offer,
        'product_offers': product_offers,
        'varient_offers': varient_offers,
        'total_offers': total_offers,
    }
    return render(request, 'vendor/offer.html', context)


def edit_varient_offers(request, id):

    selected_offer = VariationOffer.objects.get(id=id)
    form = VariationOfferForm(instance=selected_offer)
    if request.method == "POST":
        form = VariationOfferForm(data=request.POST,instance=selected_offer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Offer updated successfully')
            return redirect('view_offers')
        else:
            print(form.errors)
    
    option='Edit Varient Offer'
    check=True
    context = {
        'selected_offer':selected_offer,
        'form': form,
        'option': option,
        'check':check
    }
    return render(request,'vendor/add_offer.html', context)


def edit_product_offers(request, id=None):
    selected_offer = ProductOffer.objects.get(id=id)
    form = ProductOfferForm(instance=selected_offer)
    if request.method == "POST":
        form = ProductOfferForm(data=request.POST,instance=selected_offer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Offer updated successfully')
            return redirect('view_offers')
        else:
            print(form.errors)
            messages.success(request, 'Offer updated successfully')
    
    option='Edit Product Offer'
    check=True
    context = {
        'selected_offer':selected_offer,
        'form': form,
        'option': option,
        'check':check
    }
    return render(request,'vendor/add_offer.html', context)


def edit_vendor_offers(request, id=None):
    #Exception when there is no offer available
    try:
        selected_offer = VendorOffer.objects.get(id=id)
        form = VendorOfferForm(vendor_id=request.user.id,instance=selected_offer)
    except:
        form=VendorOfferForm(vendor_id=request.user.id)
        selected_offer=None

    if request.method == "POST":
        form = VendorOfferForm(vendor_id=request.user.id,data=request.POST,instance=selected_offer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Offer updated successfully')
            return redirect('view_offers')
        else:
            print(form.errors)
            messages.info(request, 'Something went wrong')
    
    option='Edit Vendor Offer'
    check=True
    context = {
        'form': form,
        'option': option,
        'check':check
    }
    return render(request,'vendor/add_offer.html', context)

def delete_product_offer(request, id):
    ProductOffer.objects.get(id=id).delete()
    messages.success(request,'Product offer deleted Successfully ')
    return redirect('view_offers')


def delete_variation_offer(request, id):
    VariationOffer.objects.get(id=id).delete()
    messages.success(request,'Varient offer deleted Successfully ')
    return redirect('view_offers')

def activate_variation_offer(request, id):
    selected_varient = VariationOffer.objects.get(pk=id)
    if selected_varient.is_valid:
        selected_varient.is_valid = False
        messages.success(request, "Done, Offer is not available now !")
    else:
        selected_varient.is_valid = True
        messages.success(request, "Done, Offer is available !")
    selected_varient.save()

    return redirect('view_offers')

def activate_product_offer(request, id):
    selected_product = ProductOffer.objects.get(pk=id)
    if selected_product.is_valid:
        selected_product.is_valid = False
        messages.success(request, "Done, offer is not available now !")
    else:
        selected_product.is_valid = True
        messages.success(request, "Done, offer is available !")
    selected_product.save()

    return redirect('view_offers')

def add_product_offer(request):
    vendor=request.user
    form=ProductOfferForm(vendor_id=vendor.id)
    if request.method=="POST":
        form=ProductOfferForm(vendor_id=vendor.id,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Offer added successfully')
            return redirect('view_offers')
        else:
            print(form.errors)
            messages.info(request,"something went wrong")
    context={
        'form':form
    }
    return render(request,'vendor/add_offer.html',context)

def add_variation_offer(request):
    vendor=request.user
    form=VariationOfferForm(vendor_id=vendor.id)
    if request.method=="POST":
        form=VariationOfferForm(vendor_id=vendor.id,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Offer added successfully')
            return redirect('view_offers')
        else:
            print(form.errors)
            messages.info(request,"something went wrong")
    context={
        'form':form
    }
    return render(request,'vendor/add_offer.html',context)