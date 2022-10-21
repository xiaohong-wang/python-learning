from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.utils.http import url_has_allowed_host_and_scheme
from .models import BillingProfile, Card

# Create your views here.
import stripe
stripe.api_key = "sk_test_51LsC9iHWNkoVm4NTLDuanbQX4zMqX9wxcIHOasNwEx4M8qhnuJbhAenlkLXyX1E6z51xAm20yjefqj67hwBL8ly700t6pVdyIX"
STRIPE_PUB_KEY = 'pk_test_51LsC9iHWNkoVm4NTbk2qSTQcZxC3dTCX2lGaSuAnVeOceE04hAit7KwfD1aeI4AWpmFS3bx0n1xYduz8so3g4Elh00OfuA4D5f'




def is_ajax(request):

    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def payment_method_view(request):

    billing_profile, billing_created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect('/carts')
    next_ = request.GET.get('next')
    next_url = None
    if url_has_allowed_host_and_scheme(next_, allowed_hosts=request.get_host()):
        next_url = next_

    #print('next_url',next_url)

    return render(request,'billing/payment-method.html',{'publish_key':STRIPE_PUB_KEY, 'next_url': next_url})

def payment_method_createview(request):
    if request.method == "POST" and is_ajax(request):
        billing_profile, billing_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({'message':'Cannot find this user'}, status=401)
        token = request.POST.get('token')

        new_card = Card.objects.add_new(billing_profile=billing_profile,token=token)

        return JsonResponse({'message': 'Success! Your card was added'})

    return HttpResponse('error', status=401)
