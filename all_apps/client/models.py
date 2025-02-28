from django.db import models
from django.contrib.auth import get_user_model


# get a user model
User = get_user_model()

# Create your models here.
class Client(models.Model):
        
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    website_url = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    