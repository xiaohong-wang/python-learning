"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.conf import settings
from accounts.views import login_page, register_page,logout_page, guest_register_page
from addresses.views import checkout_address_create,checkout_address_reuse
from carts.views import cart_detail_api_view
from billing.views import payment_method_view, payment_method_createview

from marketing.views import MarketingPreferenceUpdateView,MailChimpWebhookView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page,name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/',views.contact_page, name='contact'),
    path('login/', login_page,name='login'),
    path('register/', register_page, name='register'),
    path('register/guest/', guest_register_page, name='guest_register'),
    path('logout/', logout_page, name='logout'),

    path('checkout/address/create/', checkout_address_create, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse, name='checkout_address_reuse'),
    path('api/cart/', cart_detail_api_view,name='api_cart'),

    path('products/', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),
    path('carts/', include('carts.urls', namespace='carts')),
    path('accounts/', include('accounts.urls', namespace='accounts')),

    path('billing/payment-method/', payment_method_view, name='payment_method'),
    path('billing/payment-method/create/', payment_method_createview, name='payment_method_create'),

    path('settings/email/', MarketingPreferenceUpdateView.as_view(),name='marketing-pref'),

    path('webhook/mailchimp/', MailChimpWebhookView.as_view(), name='webhook-mailchimp-pref'),

]
if settings.DEBUG:
    print('static-root' + settings.STATIC_ROOT)
    print('STATIC_URL' + settings.STATIC_URL)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
