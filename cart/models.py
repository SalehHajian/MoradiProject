from django.db import models
from home.models import *
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Cart(models.Model) :
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    variant = models.ForeignKey(Variants , on_delete=models.CASCADE , null=True , blank=True)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self) :
        return self.product.name


class CartForm(ModelForm) :
    class Meta :
        model = Cart
        fields = ['quantity']


