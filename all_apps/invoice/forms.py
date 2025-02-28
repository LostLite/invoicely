from django import forms
from .models import Invoice, InvoiceItem    


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client', 
                  'title', 
                  'description', 
                  'discount_type', 
                  'discount_value', 
                  'vat_value',
                  'currency']


class InvoiceItemForm(forms.ModelForm):
    
    class Meta:
        model = InvoiceItem
        fields = ['invoice', 'item', 'description', 'quantity', 'price']