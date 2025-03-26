from django.contrib import admin
from .models import *

# Register your models here.
class Categoryadmin(admin.ModelAdmin):
    list_display=('name',"image",'description')
admin.site.register(Catagory,Categoryadmin)

admin.site.register(Product)