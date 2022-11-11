from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

from store.models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='loginpage')
def index(request):
    Wishlist = wishlist.objects.filter(user=request.user)
    context = {'Wishlist': Wishlist}
    return render(request, 'store/Wishlist.html', context)


def addtowishlist(request):
    if request.method == 'POST':
       if request.user.is_authenticated:
           prod_id = int(request.POST.get('product_id'))
           product_check = Product.objects.get(id=prod_id)
           if(product_check):
               if(wishlist.objects.filter(user=request.user, product_id=prod_id)):
                   return JsonResponse({'status': "Product already in wishlist"})
               else:
                   wishlist.objects.create(
                       user=request.user, product_id=prod_id)
                   return JsonResponse({'status': "Product added to wishlist"})
           else:
               return JsonResponse({'status': "No such Product Found"})
       else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('/')
           
                   
                
# def deletewishlistitem(request):
    