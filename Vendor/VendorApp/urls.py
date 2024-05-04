from django.urls import path
from .views import *


urlpatterns = [
    path('vendors', VendorCreateViewList.as_view(), name='vendor-view-create'),
    path('vendors/<int:pk>', VendorUpdDelFetch.as_view(), name='vendor-fetch-update-delete'),
]