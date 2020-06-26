from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
import datetime
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.http import Http404,HttpResponse,HttpResponseRedirect
from .models import Product
from carts.models import Cart
from .forms import Contactform

def home(request):

    context={
        "title":"we are here",
        "content":"Im form home page",
    }
    if request.user.is_authenticated:
        context["premium_content"] = "hiiiiii"
    return render(request,'home_page.html',context)
def about(request):
    context = {
        "title": "about page",
        "content":"im from about page"
    }
    return render(request,'home_page.html',context)


def contact(request):
    form = Contactform(request.POST or None)
    content = {
        'form':form
    }
    if form.is_valid():
        fullname = form.cleaned_data.get("fullname")
        email = form.cleaned_data.get("email")
        content = form.cleaned_data.get("content")
        messages.info(request,'contact form submitted successfully')

        return HttpResponseRedirect('/')
    else:
        form = Contactform()
    return render(request,'contact/view.html',content)

# def product_list_view(request):
#     queryset = Product.objects.all()
#     context={
#         "object_list" : queryset
#     }
#
#     return render(request,'products/product_list.html',context)

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/product_list_view.html"
    context_object_name = 'object_list'

    #function is used to show how many objects and which way  should to be displayed on template
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    # function is used to add extra content in template
    def get_context_data(self,*args, **kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        context["date"] = datetime.datetime.now()
        print(context)
        return context


def product_detail_view(request,pk=None,*args,**kwargs):
    try:
        instance = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise Http404
    except:
        print("some other error")
    # type 2
    instance = Product.objects.get_by_id(pk=pk)
    if instance is None:
        raise Http404("product does not exist")
    # type3
    queryset = Product.objects.filter(id=pk)
    if queryset.exists() and queryset.count() == 1:
        instance = queryset.first()
    else:
        raise Http404

    context={
        "object": instance
    }
    return render(request,'products/product_detail.html',context)




class ProductdetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product_detail_slug_view.html"

    def get_context_data(self,*args, **kwargs):
        context = super(ProductdetailSlugView,self).get_context_data(*args,**kwargs)
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        context["cart"] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = get_object_or_404(Product,slug=slug,active=True)
        except:
            raise Http404("object not found")
        return instance




# class ProductdetailView(DetailView):
#     # queryset = Product.objects.all()
#     template_name = "products/product_detail_view.html"
#     context_object_name = 'my_detail'
#
#     def get_context_data(self,*args, **kwargs):
#         context = super(ProductdetailView,self).get_context_data(*args,**kwargs)
#         context["date"] = datetime.datetime.now()
#         print(context)
#         return context
#
#     def get_queryset(self):
#         request = self.request
#         pk = self.kwargs.get('pk')
#         return Product.objects.filter(pk=pk)

    #to change object manager(Product.objects=self.queryset())
    # def get_object(self,*args,**kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("product does not exist")
    #     return instance



# class ProductFeaturedListView(ListView):
#     model = Product
#     template_name = "products/product_featured_list_view.html"
#
#     #function is used to show how many objects and which way  should to be displayed on template
#     def get_queryset(self):
#         return super().get_queryset().filter(featured=True,active=True)
#
# class ProductFeaturedetailView(DetailView):
#     model = Product
#     template_name = "products/product_featured_detail_view.html"
#
#     def get_queryset(self):
#         return super().get_queryset().filter(featured=True,active=True)