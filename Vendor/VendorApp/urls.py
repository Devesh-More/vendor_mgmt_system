from django.urls import path
from .views import VendorList, VendorUpdDelFetch


urlpatterns = [
    path('vendors/', VendorList.as_view(), name='vendor-view-create'),
    path('vendors/<int:pk>/', VendorUpdDelFetch.as_view(), name='vendor-fetch-update-delete'),
]