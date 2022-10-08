from django.db import models
from carts.models import Cart
from eCommerce.utils import unique_order_no_generate
from  billing.models import BillingProfile
from addresses.models import Address
# Create your models here.

ORDER_STATUS_CHOICE = {
    ('created','Created'),
    ('paid','Paid'),
    ('shipped','Shipped'),
    ('delivered','Delivered'),
    ('refund','Refund'),
}

class OrderManager(models.Manager):
    def new_or_get(self,billing_profile, cart):
        created = False
        order_obj = None

        qs = self.model.objects.filter(billing_profile=billing_profile,cart=cart,active=True)
        if qs.count() >= 1:
            order_obj = qs.first()
        else:
            order_qs = self.model.objects.filter(cart=cart, active=True)
            if order_qs.exists():
                order_qs.update(active=False)

            order_obj = Order.objects.create(cart=cart, billing_profile=billing_profile)
            created = True
        return order_obj, created




class Order(models.Model):
    order_no = models.CharField(max_length=120, blank=True)
    status = models.CharField(max_length=20, default='created', choices=ORDER_STATUS_CHOICE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active = models.BooleanField(default=True)
    billing_profile = models.ForeignKey(BillingProfile, null=True,blank=True,on_delete=models.SET_NULL)
    shipping_address = models.ForeignKey(Address, related_name='shipping_address', null=True,blank=True,on_delete=models.SET_NULL)
    billing_address = models.ForeignKey(Address,related_name='billing_address',null=True,blank=True,on_delete=models.SET_NULL)


    objects = OrderManager()
    def __str__(self):
        return self.order_no


    def check_done(self):
        if self.billing_profile and self.shipping_address and self.billing_address and self.total>0:
            return True
        return False

    def mark_paid(self):
        if self.check_done():
            self.status = 'paid'
        self.save()
        return self.status

    def save(self, *args, **kwargs):
        if not self.order_no:
            self.order_no = unique_order_no_generate(self)

        cart_obj = self.cart
        total = float(cart_obj.total) + float(self.shipping_total)
        self.total = format(total,'.2f')
        super().save(*args,**kwargs)
    """
    def order_update(self):
        cart_obj = self.cart
        self.total = cart_obj.total + self.shipping_total
        self.save()

    """
