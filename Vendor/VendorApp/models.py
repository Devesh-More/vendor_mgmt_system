from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count, Avg
from django.db.models import F
from django.db import models
from django.utils import timezone

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=250)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=30, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    class Meta:
        db_table = 'Vendor'
    
    def __str__(self) -> str:
        return self.name
    
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=150, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateField()  
    delivery_date = models.DateField(blank=True, null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=25)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateField()
    acknowledgment_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "Purchase Order"

    def __str__(self) -> str:
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    class Meta:
        db_table = "Historical Performance"


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    if instance.status == 'completed' and instance.delivered_data is None:
        instance.delivered_data = timezone.now()
        instance.save()

    # Update On-Time Delivery Rate
    completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
    # on_time_delivery_rate = completed_orders.filter(delivery_date__lte=instance.delivery_date).count() / completed_orders.count()
    on_time_deliveries = completed_orders.filter(delivery_date__gte=F('delivered_data'))
    on_time_delivery_rate = on_time_deliveries.count() / completed_orders.count()
    instance.vendor.on_time_delivery_rate = on_time_delivery_rate if on_time_delivery_rate else 0

    # Update Quality Rating Average
    completed_orders_with_rating = completed_orders.exclude(quality_rating__isnull=True)
    quality_rating_avg = completed_orders_with_rating.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0
    instance.vendor.quality_rating_avg = quality_rating_avg if quality_rating_avg else 0
    instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_response_time(sender, instance, **kwargs):
    # if instance.acknowledgment_date:
        # Update Average Response Time
        response_times = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).values_list('acknowledgment_date', 'issue_date')
        average_response_time = sum((ack_date - issue_date ).total_seconds() for ack_date, issue_date in response_times)   #/ len(response_times)
        if average_response_time < 0:
            average_response_time = 0
        if response_times:
            average_response_time = average_response_time / len(response_times)
        else:
            average_response_time = 0  # Avoid division by zero if there are no response times
        instance.vendor.average_response_time = average_response_time
        instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, **kwargs):
    # Update Fulfillment Rate
    fulfilled_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')  #, quality_rating__isnull=False)
    fulfillment_rate = fulfilled_orders.count() / PurchaseOrder.objects.filter(vendor=instance.vendor).count()
    instance.vendor.fulfillment_rate = fulfillment_rate
    instance.vendor.save()