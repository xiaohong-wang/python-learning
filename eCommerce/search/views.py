from django.shortcuts import render
from products.models import Product
from django.db.models import Q
# Create your views here.

def SearchProductView(request):
    query = request.GET.get('q',None)
    product_list = []
    if query is not None:

        product_list = Product.objects.search(query)
        print(product_list)


    context={
        'product_list':product_list,
        'query': query}
    return render(request, 'search/product_search.html', context)
