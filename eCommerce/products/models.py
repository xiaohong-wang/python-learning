from django.db import models
import random
import string
from django.utils.text import slugify
from django.urls import reverse
from django.db.models import Q


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)

    def search(self,query):
        lookups = (
                Q(name__icontains=query) |
                Q(description__icontains=query)|
                Q(tag__name__icontains=query))
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def search(self,query):

        return  self.get_queryset().active().search(query)



class Product(models.Model):
    name = models.CharField(max_length=20, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    description = models.TextField(max_length=10000, null=True)
    slug = models.SlugField(blank=True, unique=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.name +'--' + self.description[:10] +'..'

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):

        #return "/products/%s/" % self.slug
        return reverse('products:product_detail', kwargs={'slug':self.slug})

