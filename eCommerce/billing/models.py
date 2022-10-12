from django.db import models
from django.conf import settings
from accounts.models import User
from accounts.models import GuestEmail
# Create your models here.

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
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = BillingProfileManager()

    def __str__(self):
        if self.user is not None:
            if self.user.is_authenticated:
                return self.user.email
        return self.email
