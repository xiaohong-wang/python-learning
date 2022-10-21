from django.shortcuts import render, get_object_or_404
from .models import Product
from carts.models import Cart
from django.views.generic import DetailView
from analytics.mixins import ObjectViewMixin
# Create your views here.

def ProductListView(request):
    product_list = Product.objects.all()
    cart_obj,created = Cart.objects.new_or_get(request)
    #cart_product_list = cart_obj.products.all()
    return render(request, 'Products/product_list.html', {'product_list': product_list })



def ProductDetailView(request,slug):
    product_inst = get_object_or_404(Product,slug=slug)
    print(product_inst)
    cart_obj, created = Cart.objects.new_or_get(request)
    #cart_product_list = cart_obj.products.all()
   # print(request.session.session_key)

    return render(request, 'Products/product_detail.html', {'product': product_inst, 'cart_product_list':cart_product_list})


class ProductSlugDetailView(ObjectViewMixin,DetailView):
    queryset = Product.objects.all()

    template = 'Products/product_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductSlugDetailView,self).get_context_data(*args, **kwargs)
        request = self.request
        cart_obj,created = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self,*args, **kwargs):

        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            qs = Product.objects.filter(slug=slug,active=True)
        except Product.DoesNotExist:
            return Http404("Not Found")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance





