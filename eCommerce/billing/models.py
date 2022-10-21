from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from accounts.models import GuestEmail
# Create your models here.
import stripe

stripe.api_key = "sk_test_51LsC9iHWNkoVm4NTLDuanbQX4zMqX9wxcIHOasNwEx4M8qhnuJbhAenlkLXyX1E6z51xAm20yjefqj67hwBL8ly700t6pVdyIX"

User = settings.AUTH_USER_MODEL


class BillingProfileManager(models.Manager):
    def new_or_get(self,request):
        user = request.user
        obj,created= None, False
        if user.is_authenticated:
            obj, created = self.model.objects.get_or_create(user=user, email=user.email)
        else:
            guest_id = request.session.get('guest_id')
            if guest_id is not None:
                guest = GuestEmail.objects.get(pk=guest_id)
                obj, created = self.model.objects.get_or_create(email=guest.email)
            else:
                pass



        return obj,created




class BillingProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    email = models.EmailField()
    customer_id = models.CharField(max_length=120, null=True, blank=True)
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = BillingProfileManager()

    def __str__(self):
        if self.user is not None:
            if self.user.is_authenticated:
                return self.user.email
        return self.email

 
    
    def save(self,*args,**kwargs):
        if self.customer_id is None and self.email:
            customer = stripe.Customer.create(email=self.email)
            #print(customer)
            self.customer_id = customer.id

        super().save(*args,**kwargs)

    def get_cards(self):
        return self.card_set.all()

    @property
    def has_card(self):
        card_qs = self.get_cards()
        return card_qs.exists()

    @property
    def default_card(self):
        default_cards = self.card_set.filter(active=True,default=True)
        if default_cards.exists():
            return default_cards.first()

        return None

    def set_cards_inactive(self):
        cards_qs = self.get_cards()
        cards_qs.update(active=False)
        return cards_qs.filter(active=True).count()



"""
def billing_profile_created_receiver(sender, instance,*args,**kwargs):
    if instance.customer_id is None and instance.email:
        customer = stripe.Customer.create(email=instance.email)
        instance.customer_id = customer.id
        instance.save()

pre_save.connect(billing_profile_created_receiver, sender=BillingProfile)
"""
class CardManager(models.Manager):
    def all(self,*args,**kwargs):
        return self.get_queryset().filter(active=True)

    def add_new(self, billing_profile, token):
        if token:
            customer = stripe.Customer.retrieve(billing_profile.customer_id)
            stripe_card_response = stripe.Customer.create_source(customer.id, source=token)

            new_card = self.model(
                billing_profile=billing_profile,
                stripe_card_id=stripe_card_response.id,
                brand=stripe_card_response.brand,
                country=stripe_card_response.country,
                exp_month=stripe_card_response.exp_month,
                exp_year=stripe_card_response.exp_year,
                last4=stripe_card_response.last4

            )
            card_qs = billing_profile.card_set.all()
            card_qs.update(default=False)
            new_card.save()
            return new_card
        return None


class Card(models.Model):
    stripe_card_id = models.CharField(max_length=100)
    billing_profile = models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
    brand = models.CharField(max_length=20,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    exp_month = models.IntegerField(null=True,blank=True)
    exp_year = models.IntegerField(blank=True,null=True)
    last4 = models.CharField(max_length=4, null=True,blank=True)
    default = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CardManager()

    def __str__(self):
        return self.brand+'-'+self.last4

class ChargeManager(models.Manager):


    def do_charge(self,billing_profile, order_obj, card=None):
        card_obj = card

        if card_obj is None:
            cards = billing_profile.card_set.filter(default=True)
            if cards.exists():
                card_obj = cards.first()
        if card_obj is None:
            return  False, "No card is available"

        stripe_charge = stripe.Charge.create(
            amount=int(order_obj.total * 100),
            currency="usd",
            customer=billing_profile.customer_id,
            source=card_obj.stripe_card_id,
            metadata={'order_no': order_obj.order_no},
        )
        new_charge_obj = self.model(
            billing_profile=billing_profile,
            stripe_charge_id= stripe_charge.id,
            paid=stripe_charge.paid,
            refunded=stripe_charge.refunded,
            outcome=stripe_charge.outcome,
            outcome_type=stripe_charge.outcome['type'],
            seller_message=stripe_charge.outcome['seller_message'],
            risk_level=stripe_charge.outcome['risk_level'],

        )
        new_charge_obj.save()
        return new_charge_obj.paid, new_charge_obj.seller_message

class Charge(models.Model):
    billing_profile = models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
    stripe_charge_id = models.CharField(max_length=120)
    paid = models.BooleanField(default=False)
    refunded = models.BooleanField(default=False)
    outcome = models.TextField(blank=True, null=True)
    outcome_type = models.CharField(max_length=120, blank=True, null=True)
    seller_message = models.CharField(max_length=120, blank=True,null=True)
    risk_level = models.CharField(max_length=120, blank=True,null=True)


    objects = ChargeManager()


