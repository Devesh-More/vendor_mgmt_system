from django.shortcuts import render
from rest_framework import generics
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer
from django.db.models import Avg
from django.http import JsonResponse

# Create your views here.
# Vendors Create, retrive all view
class VendorCreateViewList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    

# Vendors retrive, update, delete with id view
class VendorUpdDelFetch(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


# Purchase Order Create, retrive all view
class PurchaseCreateViewList(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


# Purchase Order retrive, update, delete with id view
class PurchaseUpdDelFetch(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


