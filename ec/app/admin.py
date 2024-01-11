from django.utils.html import format_html
from django.contrib import admin
from django.urls import reverse
from . models import Cart, Product, Customer, Wishlist
# ,OrderPlaced, Payment
from django.contrib.auth.models import Group
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','mobile','state','zipcode']

@admin.register(Cart)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']
    def product(self,obj):
        link = reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html('<a href="{}"></a>',link,obj.product.title )


    # @admin.register(Payment)
    # class CustomerModelAdmin(admin.ModelAdmin):
    #     list_display=['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']


    # @admin.register(OrderPlaced)
    # class CustomerModelAdmin(admin.ModelAdmin):
    #     list_display=['id','user','customer','product','quantity','order_date','status','payment']
        


@admin.register(Wishlist)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product']
    def product(self,obj):
        link = reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html('<a href="{}"></a>',link,obj.product.title )

admin.site.unregister(Group)