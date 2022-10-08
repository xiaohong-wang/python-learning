from django.shortcuts import render,redirect
from billing.models import BillingProfile
from .models import Address
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import AddressForm
# Create your views here.

def checkout_address_create(request):
    form = AddressForm(request.POST or None)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if form.is_valid():
        #print(request.POST)
        instance = form.save(commit=False)
        billing_obj, billing_obj_created = BillingProfile.objects.new_or_get(request)
        if billing_obj is not None:
            instance.billing_profile = billing_obj
            address_type = request.POST.get('address_type')
            instance.address_type = address_type
            instance.save()
            request.session[address_type+'_address_id'] = instance.id

        else:
            return redirect('carts:checkout')
        if url_has_allowed_host_and_scheme(redirect_path,allowed_hosts=request.get_host()):
           # print(redirect_path)
           # print(instance.zip_code)
            return redirect(redirect_path)
    return redirect('carts:checkout')


def checkout_address_reuse(request):
    print('address_reuse')
    print(request.GET)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if request.user.is_authenticated:
        address_type = request.GET.get('address_type')
        address_id = request.GET.get('address_id')
        if address_type == 'shipping':
            request.session['shipping_address_id'] = address_id
        else:
            request.session['billing_address_id'] = address_id

        return redirect(redirect_path)





    return redirect('carts:checkout')