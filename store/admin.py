from django.contrib import admin
from store.models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(wishlist)