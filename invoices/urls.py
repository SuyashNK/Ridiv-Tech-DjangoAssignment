# invoices/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet, basename='invoices')
router.register(r'invoice_detail', InvoiceDetailViewSet, basename='invoice-detail')  # Use 'invoice_detail' as the endpoint name

urlpatterns = [
    path('', include(router.urls)),
]
