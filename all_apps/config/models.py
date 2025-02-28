from django.db import models

# Create your models here.
class SystemCode(models.Model):
    
    code = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.code
    
    
class SystemCodeDetail(models.Model):
    
    system_code = models.ForeignKey(SystemCode, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.code
