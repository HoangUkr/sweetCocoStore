from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Product model
class Product(models.Model):
    id  = models.AutoField(primary_key=True) # The unique ID of a cake
    name = models.CharField(max_length=50, blank=False, null=False)
    url = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default=0)
    category = models.CharField(max_length=50, blank=False, null=False, default='Cupcake')
    description = models.TextField()
    
    class Meta:
        ordering = ['name', 'price', 'id']
    
    def __str__(self) -> str:
        return f'Cake ID: {self.id}. Cake Name: {self.name}. Cake Price: {self.price}'

# Order model
class Order(models.Model):
    orderId = models.AutoField(primary_key=True) # The unique ID of Order
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    isFinish = models.BooleanField(default=False)   # Whether the order was done
    isSent = models.BooleanField(default=False) # Whether the Order was sent
    total  = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default=0)
    createdDate = models.DateTimeField(auto_now_add=True)
    sentDate = models.DateTimeField(null=True, blank=True)
    finishedDate = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['orderId', 'createdDate']
    
    def __str__(self):
        return f'Order ID: {self.orderId}. Created Date: {self.createdDate}'



# Order Item model
class OrderItem(models.Model):
    id  = models.AutoField(primary_key=True) # The unique ID
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Order Id: {self.order.orderId}. Product Name: {self.product.name}, Quantity: {self.quantity}'
    
    def subTotal(self):
        return self.quantity * self.product.price
