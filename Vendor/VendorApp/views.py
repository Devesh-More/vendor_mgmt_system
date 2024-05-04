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


# Vendors performance Matrics view
class VendorPerformanceFetch(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return JsonResponse({'on_time_delivery_rate':serializer.data['on_time_delivery_rate'],
                             'quality_rating_avg':serializer.data['quality_rating_avg'],
                             'average_response_time':serializer.data['average_response_time'],
                             'fulfillment_rate':serializer.data['fulfillment_rate']})
    

# Purchase order acknowledgement, recalculation view
class PurnchaseAcknowledgement(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        acknowledgment_date = request.data.get('acknowledgment_date')  # Getting acknowledgment_date from request data
        instance.acknowledgment_date = acknowledgment_date  # Assigned acknowledgment_date to instance
        instance.save()

        # Triggering recalculation of average_response_time for the vendor
        vendor = instance.vendor
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
        response_times = [(po.acknowledgment_date - po.issue_date).total_seconds() for po in completed_orders]
        avg_response_time = sum(response_times) / len(response_times) if len(response_times) > 0 else 0
        vendor.avg_response_time = avg_response_time
        vendor.save()

        return JsonResponse({
            'success': 'Purchase order acknowledged successfully',
            'acknowledgment_date': acknowledgment_date 
        })

