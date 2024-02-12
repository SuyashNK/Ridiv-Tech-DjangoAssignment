# invoices/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2023-01-01', 'customer_name': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)

    def test_create_invoice(self):
        url = reverse('invoices-list')
        response = self.client.post(url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invoice_list(self):
        url = reverse('invoices-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Check if the returned data contains one invoice

    def test_get_single_invoice(self):
        url = reverse('invoice-detail-detail', kwargs={'pk': self.invoice.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.invoice.id)  # Check if the returned data matches the created invoice

    def test_update_invoice(self):
        url = reverse('invoice-detail-detail', kwargs={'pk': self.invoice.id})
        updated_data = {'date': '2023-01-02', 'customer_name': 'Updated Customer'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['date'], updated_data['date'])  # Check if the date is updated

    def test_delete_invoice(self):
        url = reverse('invoice-detail-detail', kwargs={'pk': self.invoice.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)  # Check if the invoice is deleted from the database
