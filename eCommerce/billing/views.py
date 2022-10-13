from django.shortcuts import render

# Create your views here.
import stripe
stripe.api_key = "sk_test_51LsC9iHWNkoVm4NTLDuanbQX4zMqX9wxcIHOasNwEx4M8qhnuJbhAenlkLXyX1E6z51xAm20yjefqj67hwBL8ly700t6pVdyIX"
STRIPE_PUB_KEY = 'pk_test_51LsC9iHWNkoVm4NTbk2qSTQcZxC3dTCX2lGaSuAnVeOceE04hAit7KwfD1aeI4AWpmFS3bx0n1xYduz8so3g4Elh00OfuA4D5f'

def payment_method_view(request):
    if request.method == 'POST':
        print(request.post)

    return render(request,'billing/payment-method.html',{'publish_key':STRIPE_PUB_KEY})
