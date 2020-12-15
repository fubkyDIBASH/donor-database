from django.contrib import admin
from first_app.models import Name
from . import models
# Register your models here.

class SystemAdmin(admin.ModelAdmin):
    list_display = ['name','address','phoneno','bloodgroup','lastdonateddate']
   
    list_filter=['address','bloodgroup','lastdonateddate']
   

admin.site.register(Name,SystemAdmin)

