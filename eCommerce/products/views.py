from django.shortcuts import render, get_object_or_404
from .models import Product
from carts.models import Cart
from django.views.generic import DetailView
from analytics.mixins import ObjectViewMixin
# Create your views here.

def ProductListView(request):
    product_list = Product.objects.all()
    cart_obj,created = Cart.objects.new_or_get(request)
    cart_product_list = cart_obj.products.all()
    return render(request, 'Products/product_list.html', {'product_list': product_list, 'cart_product_list':cart_product_list })



def ProductDetailView(request,slug):
    product_inst = get_object_or_404(Product,slug=slug)
    cart_obj, created = Cart.objects.new_or_get(request)
    cart_product_list = cart_obj.products.all()
   # print(request.session.session_key)

    return render(request, 'Products/product_detail.html', {'product': product_inst, 'cart_product_list':cart_product_list})


class ProductSlugDetailView(ObjectViewMixin,DetailView):
    queryset = Product.objects.all()

    template = 'Products/product_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductSlugDetailView,self).get_context_data(*args, **kwargs)
        cart_obj,created = Cart.objects.new_or_get(self.request)
        cart_product_list = cart_obj.products.all()
        context['cart_product_list'] = cart_product_list
        return context

    def get_object(self,*args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            qs = Product.objects.filter(slug=slug,active=True)
        except Product.DoesNotExist:
            return Http404("Not Found")

        if qs.count() >= 1:
            instance = qs.first()

            #object_viewed_signal.send(instance.__class__, instance=instance,request=request)

            return instance




