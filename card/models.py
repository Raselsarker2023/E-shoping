from django.db import models
from django.contrib.auth.models import User
from order.models import OrderList
from products.models import ProductModel

# Create your models here.


class Cart(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_at',)
        

    def __str__(self):
        return f"Cart for {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart"

    
    
    
    
class Wishlist(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    wished_item = models.ForeignKey(OrderList,on_delete=models.CASCADE, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-added_date',]
        
        
    def __str__(self):
        return self.wished_item.product