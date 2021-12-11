from django.contrib import admin
from .models import ReviewRating, Variation, VarientColor, product
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display=('vendor_id','product_name','category','is_available','updated_at')
    prepopulated_fields = {'slug': ('product_name', )}
class VariationAdmin(admin.ModelAdmin):
    list_display=('product','varient_name','slug','ram','storage','color','image1','image2','image3','image4','price','stock')
    prepopulated_fields = {'slug': ('varient_name', )}
# class VariationAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name', )}

admin.site.register(product,productAdmin)
admin.site.register(Variation,VariationAdmin)
admin.site.register(VarientColor)
admin.site.register(ReviewRating)
# admin.site.register(Variations,VariationAdmin)
# admin.site.register(VariationItems,VariationAdmin)
# admin.site.register(VariationCategories,VariationAdmin)