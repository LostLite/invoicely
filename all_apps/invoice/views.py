from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Client, Invoice, InvoiceItem
from all_apps.config.models import SystemCodeDetail
from .forms import InvoiceForm, InvoiceItemForm
from all_apps.config import constants
from all_apps.settings.models import Currency


# Create your views here.
class InvoiceView(LoginRequiredMixin, ListView):
    model = Invoice
    context_object_name = 'invoices'
    template_name = 'invoice/index.html'
    
    def get_queryset(self):
        # get all invoices by this user
        return super().get_queryset().filter(created_by=self.request.user)
   

class InvoiceCreateView(LoginRequiredMixin, CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/invoice_form.html'
    success_url = '/invoice/'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = "Create Invoice"
        context['clients'] = Client.objects.all().filter(created_by=self.request.user)
        context['discount_types'] = SystemCodeDetail.objects.filter(system_code__code=constants.SC_DISCOUNT_TYPE)
        context['currency'] = Currency.objects.all()
        
        return context
    
    
    def form_valid(self, form):
        form.instance.invoice_status = SystemCodeDetail.objects.filter(system_code__code=constants.SC_INVOICE_STATUS, code=constants.SCD_INVOICE_STATUS_DRAFT).first()
        form.instance.created_by = self.request.user
        
        return super().form_valid(form)
    
    
    def get_success_url(self):
        messages.success(self.request, 'Invoice created successfully. Add items to the invoice.')
        return reverse_lazy('invoice_detail', kwargs={'pk': self.object.id}) 
     
     
class InvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    context_object_name = 'invoice'
    
    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user, 
                                             pk=self.kwargs['pk'])
        
    def get_template_names(self):
        
        invoice = self.get_object()
        
        if invoice.invoice_status.code != constants.SCD_INVOICE_STATUS_DRAFT:
            return ['invoice/invoice_final.html']
        return ['invoice/invoice_detail.html']
    

class InvoiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/invoice_form.html'
    success_url = '/invoice/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = "Update Invoice"
        context['clients'] = Client.objects.all()
        context['discount_types'] = SystemCodeDetail.objects.filter(system_code__code=constants.SC_DISCOUNT_TYPE)
        context['currencies'] = Currency.objects.all()
        
        return context


class SendInvoiceView(LoginRequiredMixin, View):
    
    def post(self, request, pk, *args, **kwargs):
        invoice = get_object_or_404(Invoice, pk=pk)
        
        sent_status = SystemCodeDetail.objects.filter(
            system_code__code=constants.SC_INVOICE_STATUS, 
            code=constants.SCD_INVOICE_STATUS_SENT
        ).first()
        
        if sent_status:
            invoice.invoice_status = sent_status
            invoice.sent_by = self.request.user
            invoice.sent_on = timezone.now()
        
            # save the updated invoice
            invoice.save()
            
            # send email to client
            self.send_invoice_to_client(invoice)
            
            messages.success(request, 'Invoice sent to client successfully.')
        else:
            messages.error(request, "Failed to send the invoice due to missing status.")
            
        return reverse_lazy('invoice_detail', kwargs={'pk': invoice.id})
            
    
    def send_invoice_to_client(self, invoice):
        print('Invoice forwarded to client')
        

class InvoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Invoice
    
    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)
    
    def get_success_url(self):
        messages.success(self.request, 'Invoice deleted successfully.')
        return reverse_lazy('invoice_list')


class InvoiceItemCreateView(LoginRequiredMixin, CreateView):
    model = InvoiceItem
    form_class = InvoiceItemForm
   
    def form_valid(self, form):
       form.instance.created_by = self.request.user
       return super().form_valid(form)
   
   
    def get_success_url(self):
        messages.success(self.request, 'Invoice item added successfully.')
        return reverse_lazy('invoice_detail', kwargs={'pk': self.object.invoice.id})


class InvoiceItemDeleteView(LoginRequiredMixin, DeleteView):
    model = InvoiceItem
    
    def get_success_url(self):
        messages.success(self.request, 'Invoice item deleted successfully.')
        return reverse_lazy('invoice_detail', kwargs={'pk': self.object.invoice.id})