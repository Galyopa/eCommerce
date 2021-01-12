"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from ecommerce.views import home_page, about_page, contact_page
from accounts.views import login_page, register_page, guest_register_view
from carts.views import cart_detail_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', home_page, name='home_page_url'),
    re_path(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
    re_path(r'^about/$', about_page, name='about_page_url'),
    re_path(r'^contact/$', contact_page, name='contact_page_url'),
    re_path(r'^login/$', login_page, name='login_page_url'),
    re_path(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    re_path(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
    re_path(r'^register/guest/$', guest_register_view, name='guest_register'),
    re_path(r'^register/$', register_page, name='register_page_url'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout_page_url'),
    re_path(r'^api/cart/$', cart_detail_api_view, name='api-cart_url'),
    re_path(r'^cart/', include(("carts.urls", 'cart'), namespace='cart')),
    re_path(r'^products/', include(("products.urls", 'products'), namespace='products')),
    re_path(r'^search/', include(("search.urls", 'search'), namespace='search')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
