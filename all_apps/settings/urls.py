from django.urls import path
from . import views

urlpatterns = [
    
    # settings URL patterns
    path('currency/', views.CurrencyListView.as_view(), name='currency_list'),
    path('currency/create/', views.CurrencyCreateView.as_view(), name='currency_create'),
    path('currency/update/<int:pk>/', views.CurrencyUpdateView.as_view(), name='currency_update'),
    path('currency/delete/<int:pk>/', views.CurrencyDeleteView.as_view(), name='currency_delete'),
]