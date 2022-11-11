from django.urls import path
from .import views
from store.controller import authview, cart, Wishlist

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.Collections, name="collections"),
    path('collections/<str:slug>', views.Collectionsviews, name="collectionsviews"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.Productview, name="Productview"),
    
    
    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logoutpage"),
    
    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
   
   
    path('Wishlists', Wishlist.index, name="Wishlists"),
    path('add-to-wishlist', Wishlist.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item', Wishlist.deletewishlistitem, name="deletewishlistitem"),
    
    
]
