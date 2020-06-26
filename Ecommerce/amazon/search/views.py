from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView,DetailView
from products.models import Product

# Create your views here.
class SearchProductListView(ListView):
    template_name = "search/view.html"

    def get_context_data(self,*args,**kwargs):
        context = super(SearchProductListView,self).get_context_data(*args,**kwargs)
        query = self.request.GET.get('q')
        context["query"] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)  # method_dict['q']
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()

        # if query is not None:
        #     lookup = Q(title__iexact=query)|Q(description__iexact=query)
        #     queryset = Product.objects.filter(lookup).distinct()
        # return Product.objects.all()
        # return Product.objects.filter(featured=True,active=True)


