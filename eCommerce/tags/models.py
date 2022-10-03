from django.db import models
from products.models import Product
import datetime
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    acitve = models.BooleanField(default=True)
    product = models.ManyToManyField(Product,blank=True)


    def __str__(self):
        return self.name
