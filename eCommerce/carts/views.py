from django.shortcuts import render
from products.models import Product
from .models import Cart
# Create your views here.

def cart_home(request):
    cart = Cart.objects.create(request)
    print (cart.id)





