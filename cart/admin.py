from django.contrib import admin
from .models import Cart
# Register your models here.
class CartAdmin(admin.ModelAdmin) :
    list_display =['user' , 'product' , 'variant' , 'quantity']



admin.site.register(Cart , CartAdmin)
