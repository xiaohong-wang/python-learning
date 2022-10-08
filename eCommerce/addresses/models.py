from django.db import models
from billing.models import BillingProfile
# Create your models here.



ADDRESS_TYPES=(
    ('shipping','Shipping'),
    ('billing', 'Billing'),
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.PROTECT)
    address_type = models.CharField(max_length=20, choices=ADDRESS_TYPES)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120,blank=True,null=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default='United States of America')
    state = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return str(self.billing_profile)

