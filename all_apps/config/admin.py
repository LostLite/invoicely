from django.contrib import admin
from .models import SystemCode, SystemCodeDetail

# Register your models here.
class SystemCodeConfigAdmin(admin.ModelAdmin):
    list_display = ['code', 'description']


admin.site.register(SystemCode, SystemCodeConfigAdmin)

class SystemCodeDetailConfigAdmin(admin.ModelAdmin):
    list_display = ['system_code','code', 'description']


admin.site.register(SystemCodeDetail, SystemCodeDetailConfigAdmin)