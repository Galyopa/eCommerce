from django.urls import re_path

from products.views import (
    ProductListView,
    ProductDetailSlugView
)

urlpatterns = [
    re_path(r'^$', ProductListView.as_view(), name='products_page_url'),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='product_detail_page_url'),
]
