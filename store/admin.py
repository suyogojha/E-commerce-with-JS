from django.contrib import admin
from store.models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)