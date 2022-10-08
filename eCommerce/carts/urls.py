from django.urls import path
from . import views
app_name ='carts'

urlpatterns = [
    path('', views.cart_home, name='home'),
    path('update/', views.cart_update,name='update'),
    path('checkout/', views.order_checkout, name='checkout'),
    path('checkout/done/', views.checkout_done, name='success')


    ]