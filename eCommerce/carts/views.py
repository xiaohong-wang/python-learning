from django.shortcuts import render,redirect,get_object_or_404
from products.models import Product
from .models import Cart, Item
from orders.models import Order
from accounts.forms import LoginForm, GuestForm
from billing.models import BillingProfile, Card, Charge
from accounts.models import GuestEmail
from addresses.forms import AddressForm
from addresses.models import Address
from django.http import JsonResponse
# Create your views here.
import stripe
stripe.api_key = "sk_test_51LsC9iHWNkoVm4NTLDuanbQX4zMqX9wxcIHOasNwEx4M8qhnuJbhAenlkLXyX1E6z51xAm20yjefqj67hwBL8ly700t6pVdyIX"
STRIPE_PUB_KEY = 'pk_test_51LsC9iHWNkoVm4NTbk2qSTQcZxC3dTCX2lGaSuAnVeOceE04hAit7KwfD1aeI4AWpmFS3bx0n1xYduz8so3g4Elh00OfuA4D5f'



def is_ajax(request):

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

    #products_list = cart_obj.products.all()
   # cart_obj.update_total()
    items = cart_obj.item_set.all()
    context = {
       # 'products':products_list,
        'items': items,
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
            return redirect('carts:home')
        item_obj, item_created = Item.objects.new_or_get(product=product_obj, cart=cart_obj)
        cart_obj, created = Cart.objects.new_or_get(request)
        added = False
        cart_items_count = cart_obj.items_count
        request.session['cart-items_count'] = cart_items_count


        if is_ajax(request):
            #  print('Ajax request')
            json_data = {
                'added': added,
                'cartItemCount': cart_items_count

            }
            return JsonResponse(json_data, status=200)




    """
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

    """
    return redirect('carts:home')

def cart_item_delete(request):
    item_id = request.POST.get('item_id')
    item = get_object_or_404(Item,pk=item_id)

    item.delete()


    return redirect('carts:home')


def order_checkout(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)

    if cart_obj.item_set.count() == 0:
        return redirect('carts:home')

    login_form = LoginForm()
    guest_form = GuestForm()
    address_qs = None
    address_form = AddressForm()
    order_obj = None
    has_card = None
    billing_obj = None
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
    print(billing_obj)

    billing_obj,billing_obj_created = BillingProfile.objects.new_or_get(request)
    print(billing_obj)
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

        has_card = billing_obj.has_card


        if request.method == 'POST':
            is_ready = order_obj.check_done
            if is_ready:
                is_paid, charge_msg = Charge.objects.do_charge(order_obj=order_obj,billing_profile=billing_obj)
                if  is_paid:
                    order_obj.mark_paid()
                    request.session['cart_item'] = 0
                    del request.session['cart_id']
                    if request.session.get('guest_id') is not None:
                        del request.session['guest_id']

                    if not billing_obj.user:
                        billing_obj.set_cards_inactive()

                    return redirect('carts:success')
                else:

                    print(charge_msg)
                    return redirect("carts:checkout")





    context = {
        'order_obj': order_obj,
        'cart_obj': cart_obj,
        'login_form': login_form,
        'guest_form': guest_form,
        'billing_obj': billing_obj,
        'address_form':address_form,
        'address_qs': address_qs,
        'has_card': has_card,
        'publish_key':STRIPE_PUB_KEY



    }


    print('checkout')


    return render(request,'carts/checkout.html',context)


def checkout_done(request):
    return render(request,'carts/checkout_done.html', {})




