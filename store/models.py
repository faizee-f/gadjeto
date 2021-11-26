from io import BytesIO
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from category.models import category, sub_category, variants
from django.urls import reverse

from vendors.models import Vendors
# Create your models here.

class product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendors,on_delete=CASCADE)
    product_name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=200,blank=True)
    image1 =models.ImageField(upload_to='photos/product',blank=True)
    image2 =models.ImageField(upload_to='photos/product',blank=True)
    image3 =models.ImageField(upload_to='photos/product',blank=True)
    thumbnail=models.ImageField(upload_to='photos/product',blank=True,null=True)
    is_available=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    modified_date=models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.product_name



class VarientColor(models.Model):
    color_name=models.CharField(max_length=50,unique=True)

    def __str__ (self):
        return self.color_name


# class VariationManager(models.Manager):
#     def colors(self):
#         return super(VariationManager,self).values('color').distinct()


#RAM CHOICE

MOBILE_RAM_CHOICE=(
    ("2 GB","2 GB"),
    ("4 GB","4 GB"),
    ("6 GB","6 GB"),
    ("8 GB","8 GB"),
    ("12 GB","12 GB"),    
)

MOBILE_STRG_CHOICE=(
    ("16 GB","16 GB"),
    ("32 GB","32 GB"),
    ("64 GB","64 GB"),
    ("128 GB","128 GB"),
    ("256 GB","256 GB"),
    ("512 GB","512 GB"),
    ("1 TB","1 TB"),
)

class Variation(models.Model):
    product=models.ForeignKey(product,on_delete=CASCADE,related_name='varion')
    varient_name=models.CharField(max_length=100,blank=True)
    slug=models.SlugField(max_length=100,unique=True)
    ram=models.CharField(choices=MOBILE_RAM_CHOICE,max_length=20,blank=True)
    storage=models.CharField(choices=MOBILE_STRG_CHOICE,max_length=50,blank=True)
    color=models.ForeignKey(VarientColor,on_delete= CASCADE)
    image=models.ImageField(upload_to='photos/product',blank=True)
    price=models.IntegerField(blank=True)
    stock=models.IntegerField(blank=True)
    is_available=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    modified_date=models.DateTimeField(auto_now=True,blank=True)


    # objects= VariationManager()


    def __str__ (self):
        return self.varient_name


    def get_url(self):
        return reverse('product_detail',args=[self.product.category.slug,self.product.slug,self.slug])
    # def get_thumbnail(self):
    #     if self.thumbnail:
    #         return self.thumbnail.url
    #     else:
    #         if self.image1:
    #             self.thumbnail=self.make_thumbnail(self.image1)
    #             self.save()

    #             return self.thumbnail.url

    # def make_thumbnail(self,image1,size=(300,200)):
    #     img=Image.open(image1)
    #     img.convert('RGB')
    #     img.thumbnail(size)

    #     thumb_to=BytesIO()
    #     img.save(thumb_to,'JPEG',quality=85)
    #     thumbnail=FIle(thumb_to,name=Image.name)

    #     return thumbnail

# class VariationCategories(models.Model):
#     var_category=models.ForeignKey(category,on_delete=CASCADE)
#     name=models.CharField(max_length=100)
#     slug=models.SlugField(max_length=100,unique=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering=['var_category']


#     def get_url(self):
#         return reverse('variation_category',args=[self.name.slug,self.slug])

# class VariationItems(models.Model):
#     item_category=models.ForeignKey(VariationCategories,on_delete=CASCADE)
#     name=models.CharField(max_length=100)
#     slug=models.SlugField(max_length=100,unique=True)

#     def __str__(self):
#         return self.name

#     def get_url(self):
#         return reverse('variation_category',args=[self.name.slug,self.slug])

# class Variations(models.Model):
#     product=models.ForeignKey(product,on_delete=CASCADE)
#     created_date=models.DateTimeField(auto_now_add=True,blank=True)
#     modified_date=models.DateTimeField(auto_now=True,blank=True)

#     def __unicode__(self):
#         return self.title