from django.db import models
from django.contrib.auth.models import AbstractUser
from all_apps.config.models import SystemCodeDetail

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    
    # set the email as the required username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    
    def get_first_name(self):
        """Return user first name"""
        return self.first_name
    
    
    def get_last_name(self):
        """Return user last name"""
        return self.last_name
    
    
    def get_email_address(self):
        """Return user email address"""
        return self.email
    
    
    def get_phone_number(self):
        """Return user phone number"""
        return self.phone_number

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
