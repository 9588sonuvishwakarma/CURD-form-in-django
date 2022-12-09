from django.db import models
#extra coding for practise
class Name(models.Model):
    name = models.CharField(max_length=200,null=True)
    address= models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.name
class oom(models.Model):
    phone = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.phone

class Fast(models.Model):
    speed = (
        ('slow','slow'),
        ('modrate','modrate')
    )

    num = models.ForeignKey(Name,null=True, on_delete=models.SET_NULL)
    Speeds = models.CharField(max_length=200,null=True,choices=speed)

# Create your models here.

class Customer(models.Model):

    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    date_create = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('indoor','indoor'),
        ('out Door','out Door'),
    )
    name  = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    # to make relationship by tag
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('Delivered','Delivered'),
    )
    #to make relationship
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)

    product =models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
# create order ..........................................
from django.forms import ModelForm
from .models import Order
class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = '__all__'
        # you can use the all and type the one by one
        fields = ['customer','product','status']

# class cold(models.Model):
#     name = models.CharField(max_length=100)
#     amount = models.CharField(max_length=100)
#     oder_id =models.CharField(max_length=100,blank=True)
#     razorpay_id = models.CharField(max_length=100,blank=True)
#     paid = models.BooleanField(default=False)

# import django_filters
# from .models import Order
# class OrderFilter(django_filters.FilterSet):
#     class Meta:
#         model = Order
#         fields = '__all__'
