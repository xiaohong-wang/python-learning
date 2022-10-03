from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.conf import settings
import datetime
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User,models.SET_NULL, blank=True, null=True)
    products = models.ManyToManyField(Product, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)

    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('cart')
        print (cart)
        if cart is None:
           cart = self.session['cart'] = {}

        self.cart = cart

    def add(self,product,quantity=1, update_quantity=False):
        product_id = product.id
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}

        else:
            if update_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True





    def __str__(self):
        return str(self.id)