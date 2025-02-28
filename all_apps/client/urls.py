from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all-clients'),       
    path('add/', views.add_client, name='add-client'),       
    path('edit/<int:pk>', views.update_client, name='edit-client'),       
    path('delete/<int:pk>', views.delete_client, name='delete-client'),       
]
