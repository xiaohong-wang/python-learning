from django.db import models
from accounts.models import User
from products.models import Product
from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed
import datetime

# Create your models here.
User = settings.AUTH_USER_MODEL
"""  

class CartManager(models.Manager):
    def new(self,user=None):
        user_obj = None
        if user.is_authenticated:
            user_obj = user

        return Cart.objects.create(user=user_obj)

    def new_or_get(self,request):
        cart_id = request.session.get('cart_id',None)
        qs = self.get_queryset() .filter(pk=cart_id)
        created = True
        if qs.count() == 1:
            cart_obj = qs.first()
            created = False
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(request.user)
            request.session['cart_id'] = cart_obj.id
        return (cart_obj, created)




class Cart(models.Model):
    user = models.ForeignKey(User,models.SET_NULL, blank=True, null=True)
    products = models.ManyToManyField(Product, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    objects = CartManager()



    def __str__(self):
        return str(self.id)

    def update_total(self):

        product_list = self.products.all()
        self.subtotal = 0
        for product in product_list:
            self.subtotal += product.price

        self.total = float(self.subtotal) * 1.08
        self.total = "{:.2f}".format(self.total)

        self.save()
        
        
"""



class CartManager(models.Manager):

    def new(self,user=None):
        user_obj = None
        if user.is_authenticated:
            user_obj = user
        return Cart.objects.create(user=user_obj)

    def new_or_get(self,request):
        cart_id = request.session.get('cart_id',None)
        created = True
        qs = self.get_queryset().filter(pk=cart_id)
        if qs.count() >= 1:
            cart_obj = qs.first()
            created = False
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            request.session['cart_id'] = cart_obj.id

        return cart_obj,created




class Cart(models.Model):
    user = models.ForeignKey(User,models.SET_NULL, blank=True, null=True)
   # products = models.ManyToManyField(Product, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    items_count = models.PositiveIntegerField(default=0)

    objects = CartManager()

    def __str__(self):
        return str(self.id)






"""
    def save(self,*args,**kwargs):
        self.subtotal = 0
        self.items_count =0
        for item in self.item_set.all():
            self.subtotal += item.total_price
            self.items_count += item.quantity
        self.total = float(self.subtotal) * 1.08
        self.total = "{:.2f}".format(self.total)
        super().save(*args, **kwargs)
"""





class ItemManager(models.Manager):

    def new_or_get(self,cart,product):
        item_obj,created = None, True
        item_qs = self.get_queryset().filter(product=product, cart=cart)
        if item_qs.count() >= 1 :
            item_obj = item_qs.first()
            created = False
            item_obj.quantity += 1

        else:
            item_obj = Item.objects.create(product=product,cart=cart, quantity=1)

        item_obj.save()
        return item_obj,created


class Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    unite_price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total_price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)


    objects = ItemManager()

    def __str__(self):
        return str(self.product.name)+'--' + str(self.quantity)

    def save(self,*args,**kwargs):
        self.unite_price = self.product.price
        self.total_price = self.quantity * self.unite_price
        super().save(*args, **kwargs)





def post_save_cart_receiver(sender, instance,*args, **kwargs):

    cart_obj = Cart.objects.get(pk=instance.cart.id)
    cart_obj.subtotal = 0
    cart_obj.items_count = 0
    for item in cart_obj.item_set.all():
        cart_obj.subtotal += item.total_price
        cart_obj.items_count += item.quantity

    cart_obj.total = float(cart_obj.subtotal) * 1.08
    cart_obj.total = "{:.2f}".format(cart_obj.total)

    cart_obj.save()


post_save.connect(post_save_cart_receiver, sender=Item)




"""
def pre_save_item_receiver(sender, instance, *args, **kwargs):
    instance.unite_price = instance.product.price
    instance.total_price = instance.quantity * instance.unite_price



pre_save.connect(pre_save_item_receiver, sender=Item)

"""

