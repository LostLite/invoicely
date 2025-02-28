from django.urls import path
from . import views

urlpatterns = [
    
    # unviuce URL patterns
    path('', views.InvoiceView.as_view(), name='invoice_list'),
    path('create/', views.InvoiceCreateView.as_view(), name='invoice_create'),
    path('detail/<int:pk>', views.InvoiceDetailView.as_view(), name='invoice_detail'),
    path('update/<int:pk>', views.InvoiceUpdateView.as_view(), name='invoice_update'),
    path('send-invoice/<int:pk>', views.SendInvoiceView.as_view(), name='invoice_send'),
    path('delete/<int:pk>', views.InvoiceDeleteView.as_view(), name='invoice_delete'),
    
    # Invoice Item URL patterns
    path('item/create/', views.InvoiceItemCreateView.as_view(), name='invoice_item_create'),
    path('item/delete/<int:pk>', views.InvoiceItemDeleteView.as_view(), name='invoice_item_delete'),
    
]
