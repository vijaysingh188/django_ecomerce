"""amazon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from products.views import (home,about,contact,ProductListView,product_detail_view,ProductdetailSlugView)
from accounts.views import (login_form,register_form,logout_request,guest_register_view)



urlpatterns = [
    url(r'^$',home,name="home"),
    url(r'^about/',about,name="about"),
    url(r'^contact/',contact,name="contact"),

    url(r'^login/',login_form,name="login"),
    url(r'^register/guest_register/',guest_register_view,name="guest_register"),
    url(r'logout/',logout_request,name="logout"),
    url(r'^register/',register_form,name="register"),

    url(r'^products/',include("products.urls",namespace="products")),
    url(r'^search/',include("search.urls",namespace="search")),
    url(r'^cart/',include("carts.urls",namespace="cart")),

    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

