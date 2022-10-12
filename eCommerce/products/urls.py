from django.urls import path
from . import views
from .views import ProductSlugDetailView
app_name ='products'

urlpatterns = [
    path('', views.ProductListView, name='product_list'),
    #path('<slug:slug>/', views.ProductDetailView, name='product_detail'),
    path('<slug:slug>/', ProductSlugDetailView.as_view(), name='product_detail')

    ]