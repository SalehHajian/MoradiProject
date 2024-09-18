from django.db import models
from django.contrib.auth.models import User
from home.models import *
from django.forms import ModelForm
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    email = models.EmailField()
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)

    def __str__(self) :
        return self.user.username


class ItemOrder(models.Model) :
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    variant = models.ForeignKey(Variants , on_delete= models.CASCADE , null=True , blank=True)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self) :
        return self.user.username




class OrderForm(ModelForm) :
    class Meta :
        model = Order
        fields = ['email' , 'f_name' , 'l_name' , 'address']