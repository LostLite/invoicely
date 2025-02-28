from django.db import models
from django.contrib.auth import get_user_model
from all_apps.client.models import Client
from all_apps.config.models import SystemCodeDetail
from all_apps.settings.models import Currency


# get a user model
User = get_user_model()

# Create your models here.

class Invoice(models.Model):
    
    client = models.ForeignKey(Client, related_name='invoices', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    invoice_status = models.ForeignKey(SystemCodeDetail, related_name='invoice_status', on_delete=models.DO_NOTHING)
    discount_type = models.ForeignKey(SystemCodeDetail, related_name='discount_type', on_delete=models.DO_NOTHING)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    vat_value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, related_name='currencies', on_delete=models.DO_NOTHING, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='invoices_created', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_by = models.ForeignKey(User, related_name='invoices_sent', on_delete=models.DO_NOTHING, null=True, blank=True)
    sent_on = models.DateTimeField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    
    def get_sub_total(self):
        total = 0
        for item in self.items.all():
            total += item.get_total()
        return total
    
    
    def get_discount(self):
        if self.discount_type.code == 'Percentage':
            return self.get_sub_total() * (self.discount_value / 100)
        return self.discount_value
    
    
    def get_vat(self):
        return (self.get_sub_total() - self.get_discount()) * (self.vat_value / 100)
    
    
    def get_total(self):
        return round((self.get_sub_total() - self.get_discount()) + self.get_vat(), 2)
    
    
class InvoiceItem(models.Model):
    
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, related_name='invoice_items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description
    
    def get_total(self):
        return self.quantity * self.price
    
    
class InvoicePayment(models.Model):
    
    invoice = models.ForeignKey(Invoice, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    created_by = models.ForeignKey(User, related_name='invoice_payments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.amount
    
    