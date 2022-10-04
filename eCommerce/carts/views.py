from django.shortcuts import render,redirect
from products.models import Product
from .models import Cart
# Create your views here.


def cart_home(request):
    """
    cart_id = request.session.get('cart_id',None)
    print('cart_id:', cart_id)

    qs = Cart.objects.filter(pk=cart_id)
    if qs.count() == 1:
        print ("Cart ID exists")
        cart = qs.first()
        if request.user.is_authenticated and cart.user is None:
            cart.user = request.user
            cart.save()

    else:
        cart = Cart.objects.new(request.user)
        request.session['cart_id'] = cart.id
        print("Create New Cart, cart id is:", request.session['cart_id'])

    """
    cart_obj = Cart.objects.new_or_get(request)
    #print (request.session['cart_id'], cart_obj.id)
    total = 0
    products_list = cart_obj.products.all()
    for product in products_list:
        total += product.price


    return render(request,'carts/newcart.html',{"products":products_list, 'total':total})




def cart_update(request):
    product_id = request.POST.get('product_id')
    #print(product_id)
    cart_obj = Cart.objects.new_or_get(request)
    if product_id is not None:
        try:
            product_obj = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            print("Product is gone")
            return  redirect('carts:home')
        if product_obj not in cart_obj.products.all():
            cart_obj.products.add(product_obj)
        else:
            cart_obj.products.remove(product_obj)

    return redirect('carts:home')

