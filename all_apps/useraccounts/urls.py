from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_profile, name='user-profile'),
    path('edit',views.edit_user_details, name='user-profile-edit'),
    path('changepassword',views.change_user_password, name='user-profile-change-password'),
    
]
