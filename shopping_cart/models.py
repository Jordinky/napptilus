from django.conf import settings
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(max_length=200)
    img_url = models.URLField(max_length=200)
    price = models.FloatField(max_length=200)
    initial_stock = models.IntegerField()
    actual_stock = models.IntegerField(default = 0)
    description = models.CharField(max_length=200)
    primary_color = models.CharField(max_length=200)
    secondary_color = models.CharField(max_length=200)
    brand = models.CharField(max_length=200,default = '')
    size = models.CharField(max_length=4) 

    def __str__(self):
        return self.name

class Cap(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, default=0)
    logoColor = models.CharField(max_length=200)

    def __str__(self):
        return self.product.name

class Tee(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, default=0)
    typeOfFabric = models.CharField(max_length=200)
    sizing = models.CharField(max_length=200)
    sleeves = models.CharField(max_length=200)

    def __str__(self):
        return self.product.name
    
class Cart(models.Model):
    date = models.DateField(max_length=200)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.completed

class CartProduct(models.Model):
    product = models.ForeignKey(Product, default = 0, on_delete= models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=2,default=0)

    def __str__(self):
        return self.product.name
