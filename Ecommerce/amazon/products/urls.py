from django.conf.urls import url
from .views import (ProductListView,
                    ProductdetailSlugView,)

app_name = 'products'

urlpatterns = [
    url(r'^$',ProductListView.as_view(),name="List"),
    url(r'^(?P<slug>[-\w]+)/$',ProductdetailSlugView.as_view(),name="Detail"),
]















