from django.urls import re_path

from carts.views import cart_home, cart_update, checkout_home, checkout_done_view

urlpatterns = [
    re_path(r'^$', cart_home, name='home_url'),
    re_path(r'^checkout/$', checkout_home, name='checkout_url'),
    re_path(r'^update/$', cart_update, name='update_url'),
    re_path(r'^success/$', checkout_done_view, name='success_url'),
]
