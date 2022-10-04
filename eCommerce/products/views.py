from django.shortcuts import render, get_object_or_404
from .models import Product
from carts.models import Cart
# Create your views here.

def ProductListView(request):
    product_list = Product.objects.all()
    cart_obj = Cart.objects.new_or_get(request)
    print(request.session.session_key)
    return render(request, 'Products/product_list.html', {'product_list': product_list, 'cart_obj':cart_obj})



def ProductDetailView(request,slug):
    product_inst = get_object_or_404(Product,slug=slug)
    print(request.session.session_key)

    return render(request, 'Products/product_detail.html', {'product': product_inst})