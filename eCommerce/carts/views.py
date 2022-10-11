from django.shortcuts import render,redirect
from products.models import Product
from .models import Cart
from orders.models import Order
from accounts.forms import LoginForm, GuestForm
from billing.models import BillingProfile
from accounts.models import GuestEmail
from addresses.forms import AddressForm
from addresses.models import Address
from django.http import JsonResponse
# Create your views here.



def is_ajax(request):
    print('called')
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


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

    cart_obj, created = Cart.objects.new_or_get(request)
    #print (request.session['cart_id'], cart_obj.id)

    products_list = cart_obj.products.all()
    cart_obj.update_total()
    context = {
        'products':products_list,
        'total': cart_obj.total,
        'subtotal':cart_obj.subtotal,

    }


    return render(request,'carts/newcart.html',context)


def cart_detail_api_view(reqeust):
    cart_obj, created = Cart.objects.new_or_get(reqeust)
    products = [{
        'name':x.name,
        'price':x.price,
        'url':x.get_absolute_url(),
        'id':x.id
        }
        for x in cart_obj.products.all()]
    cart_data = {
        'products':products,
        'subtotal':cart_obj.subtotal,
        'total':cart_obj.total

    }


    return JsonResponse(cart_data)


def cart_update(request):
    product_id = request.POST.get('product_id')
    #print(product_id)
    cart_obj,created = Cart.objects.new_or_get(request)

    if product_id is not None:
        try:
            product_obj = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:

            return  redirect('carts:home')
        if product_obj not in cart_obj.products.all():
            cart_obj.products.add(product_obj)
            added = True
        else:
            cart_obj.products.remove(product_obj)
            added = False

        request.session['cart_item'] = cart_obj.products.count()

        if is_ajax(request):
          #  print('Ajax request')
            json_data = {
                'added': added,
                'removed': not added,
                'cartItemCount': cart_obj.products.count(),

            }
            return JsonResponse(json_data,status=200)


    return redirect('carts:home')


def order_checkout(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)

    #print('cart_created', cart_created)

    #order_obj = None
    if cart_obj.products.count() == 0:
     #   print('cart is empty')
        return redirect('carts:home')

         #   order_obj.order_update()
        #order_obj.save()
    login_form = LoginForm()
    guest_form = GuestForm()
    address_qs = None
    address_form = AddressForm()
    order_obj = None
    shipping_address_id = request.session.get('shipping_address_id', None)
    billing_address_id = request.session.get('billing_address_id', None)

    #billing_obj = None
    #user = request.user
    #guest_id = request.session.get('guest_id')
   # print('guest', guest_id)
    """
    if request.user.is_authenticated:
        print (user)
        billing_obj, billing_obj_created = BillingProfile.objects.get_or_create(user=user,email=user.email)

    elif guest_id is not None:

        guest = GuestEmail.objects.get(pk=guest_id)
        print('guest', guest_id)
        billing_obj, billing_obj_created = BillingProfile.objects.get_or_create(email=guest.email )
    else:
        pass
    """
    billing_obj,billing_obj_created = BillingProfile.objects.new_or_get(request)
    """
    if billing_obj is not None:
        order_qs = Order.objects.filter(cart=cart_obj,active=True)
        if order_qs.exists():
            order_qs.update(active=False)

        order_obj = Order.objects.create(cart=cart_obj,billing_profile=billing_obj)
        print(order_obj)
    """
    if billing_obj is not None:
        if request.user.is_authenticated:
            address_qs = billing_obj.address_set.all()


        order_obj,order_obj_created = Order.objects.new_or_get(billing_profile=billing_obj,cart=cart_obj)


   # print('shipping_address_id', shipping_address_id)

        if shipping_address_id is not None:
            order_obj.shipping_address = Address.objects.get(pk=shipping_address_id)
            order_obj.save()
            del request.session['shipping_address_id']
        if billing_address_id is not None:
            order_obj.billing_address = Address.objects.get(pk=billing_address_id)
            order_obj.save()
            del request.session['billing_address_id']

        if request.method == 'POST':
            if order_obj.check_done:
                order_obj.mark_paid()
                request.session['cart_item'] = 0
                del request.session['cart_id']

                return redirect('carts:success')



    context = {
        'order_obj': order_obj,
        'cart_obj': cart_obj,
        'login_form': login_form,
        'guest_form': guest_form,
        'billing_obj': billing_obj,
        'address_form':address_form,
        'address_qs': address_qs,



    }


    print('checkout')


    return render(request,'carts/checkout.html',context)


def checkout_done(request):
    return render(request,'carts/checkout_done.html', {})




