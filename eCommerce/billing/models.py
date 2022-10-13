from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from accounts.models import GuestEmail
# Create your models here.
import stripe

stripe.api_key = "sk_test_51LsC9iHWNkoVm4NTLDuanbQX4zMqX9wxcIHOasNwEx4M8qhnuJbhAenlkLXyX1E6z51xAm20yjefqj67hwBL8ly700t6pVdyIX"

User = settings.AUTH_USER_MODEL


class  BillingProfileManager(models.Manager):
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

"""
def billing_profile_created_receiver(sender, instance,*args,**kwargs):
    if instance.customer_id is None and instance.email:
        customer = stripe.Customer.create(email=instance.email)
        instance.customer_id = customer.id
        instance.save()

pre_save.connect(billing_profile_created_receiver, sender=BillingProfile)
"""
