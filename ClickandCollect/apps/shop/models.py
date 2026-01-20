from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

class CartItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def total_price(self):
        total=self.product.price*self.quantity
        return total
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"