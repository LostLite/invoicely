from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

# Create your models here.
class Currency(models.Model):
    
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='currencies', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name