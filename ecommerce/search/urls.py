from django.urls import re_path

from search.views import SearchProductView

urlpatterns = [
    re_path(r'^$', SearchProductView.as_view(), name='query'),
]
