from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.conf import settings
import datetime
# Create your models here.

class CartManager(models.Manager):
    def new(self,user=None):
        user_obj = None
        if user.is_authenticated:
            user_obj = user

        return Cart.objects.create(user=user_obj)

    def new_or_get(self,request):
        cart_id = request.session.get('cart_id',None)
        qs = Cart.objects.filter(pk=cart_id)
        if qs.count() == 1:
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(request.user)
            request.session['cart_id'] = cart_obj.id
        return cart_obj


class Cart(models.Model):
    user = models.ForeignKey(User,models.SET_NULL, blank=True, null=True)
    products = models.ManyToManyField(Product, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)

    objects = CartManager()



    def __str__(self):
        return str(self.id)