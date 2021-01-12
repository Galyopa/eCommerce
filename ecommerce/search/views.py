from django.views.generic import ListView

from products.models import Product


class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        contex = super(SearchProductView, self).get_context_data(*args, **kwargs)
        contex['query'] = self.request.GET.get('q')
        return contex

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
