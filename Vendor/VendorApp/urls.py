from django.urls import path
from .views import *


urlpatterns = [
    path('vendors', VendorCreateViewList.as_view(), name='vendor-view-create'),
    path('vendors/<int:pk>', VendorUpdDelFetch.as_view(), name='vendor-fetch-update-delete'),
    path('purchase_order', PurchaseCreateViewList.as_view(), name='purchase-view-create'),
    path('purchase_order/<int:pk>', PurchaseUpdDelFetch.as_view(), name='purchase-fetch-update-delete'),
    path('vendors/<int:pk>/performance', VendorPerformanceFetch.as_view(), name='vendor-performance-matrics'),
    path('purchase_orders/<int:pk>/acknowledge', PurnchaseAcknowledgement.as_view(), name='purnchase-acknowledge'),

]