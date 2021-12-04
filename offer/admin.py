from django.contrib import admin

from offer.models import CategoryOffer, Coupen, ProductOffer, RedeemedCoupen, SubCategoryOffer, VariationOffer, VendorOffer

# Register your models here.


admin.site.register(CategoryOffer)
admin.site.register(SubCategoryOffer)
admin.site.register(VendorOffer)
admin.site.register(ProductOffer)
admin.site.register(VariationOffer)

admin.site.register(Coupen)
admin.site.register(RedeemedCoupen)