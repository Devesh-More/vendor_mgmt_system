from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Avg
from django.db import models


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
def update_metrics(sender, instance, created, **kwargs):
    # On-Time Delivery Rate
    if instance.status == 'completed':
        completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
        on_time_deliveries = completed_orders.filter(delivery_date__lte=instance.delivery_date)
        on_time_delivery_rate = on_time_deliveries.count() / completed_orders.count() if completed_orders.count() > 0 else 0 
        instance.vendor.on_time_delivery_rate = on_time_delivery_rate
        instance.vendor.save()

    # Quality Rating Average
    if instance.status == 'completed' and instance.quality_rating is not None:
        completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
        avg_quality_rating = completed_orders.aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating']
        instance.vendor.quality_rating_average = avg_quality_rating
        instance.vendor.save()

@receiver(pre_save, sender=PurchaseOrder)
def calculate_average_response_time(sender, instance, **kwargs):
    if instance.acknowledgment_date is not None:
        completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False)
        response_times = [(po.acknowledgment_date - po.issue_date).total_seconds() for po in completed_orders]
        avg_response_time = sum(response_times) / len(response_times) if len(response_times) > 0 else 0
        instance.vendor.avg_response_time = avg_response_time
        instance.vendor.save() 


@receiver(post_save, sender=PurchaseOrder)
def calculate_fulfilment_rate(sender, instance, created, **kwargs):
    total_orders = PurchaseOrder.objects.filter(vendor=instance.vendor).count()
    successful_fulfillments = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed', quality_rating__isnull=False)
    fulfilment_rate = successful_fulfillments.count() / total_orders if total_orders > 0 else 0
    instance.vendor.fulfilment_rate = fulfilment_rate
    instance.vendor.save()
