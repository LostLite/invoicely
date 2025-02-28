from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Currency


# Create your views here.
class CurrencyListView(LoginRequiredMixin, ListView):
    model = Currency
    context_object_name = 'currencies'
    template_name = 'settings/currency/currency_list.html'
    
    
    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)
    
    
class CurrencyCreateView(LoginRequiredMixin, CreateView):
    model = Currency
    fields = ['name', 'symbol']
    template_name = 'settings/currency/currency_form.html'
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = "Add Currency"
        return context
    
    def get_success_url(self):
        messages.success(self.request, 'Currency created successfully.')
        return reverse_lazy('currency_list')
    
    
class CurrencyUpdateView(LoginRequiredMixin, UpdateView):
    model = Currency
    fields = ['name', 'symbol']
    template_name = 'settings/currency/currency_form.html'
    
    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = "Update Currency"
        return context
    
    def get_success_url(self):
        messages.success(self.request, 'Currency updated successfully.')
        return reverse_lazy('currency_list')
    

class CurrencyDeleteView(LoginRequiredMixin, DeleteView):
    model = Currency
    
    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)
    
    def get_success_url(self):
        messages.success(self.request, 'Currency deleted successfully.')
        return reverse_lazy('currency_list')