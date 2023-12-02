from django.contrib import admin
from .models import *

# admin.site.register((Maincategory,Subcategory,Brand,Product,Buyer,Wishlist,Checkout,CheckoutProduct,Newslatter,Contact))

@admin.register(Maincategory)
class MaincategoryAdmin(admin.ModelAdmin):
    list_display=["id","name"]

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display=["id","name"]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=["id","name","pic"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["id","name","maincategory","Subcategory","Brand","color","size","baseprice","discount","finalprice","stock","description","pic1","pic2","pic3","pic4"]


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display=["id","name","username","email","phone","address","pin","city","state"]

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display=["id","buyer","product"]

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display=["id","buyer","orderStatus","paymentStatus","paymentMode","subtotal","shipping","total","date","rppid"]

@admin.register(CheckoutProduct)
class CheckoutProductAdmin(admin.ModelAdmin):
    list_display=["id","checkout","product"]

@admin.register(Newslatter)
class NewslatterAdmin(admin.ModelAdmin):
    list_display=["id","email"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=["id","name","email","subject","message","status","date"]

    
