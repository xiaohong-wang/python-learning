from django.urls import path
from . import views
app_name ='products'

urlpatterns = [
    path('', views.ProductListView, name='product_list'),
    path('<slug:slug>/', views.ProductDetailView, name='product_detail'),

    ]