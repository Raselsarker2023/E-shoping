from django.db import models
from django.contrib.auth.models import User
from products.models import ProductModel

# Create your models here.

class Cart(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_at',)
        

    def __str__(self):
        return f"Cart for {self.user_name}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    produce_name = models.CharField(max_length=15, null=True, blank=True)
    product_image_url = models.URLField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart"

    
    
class Wishlist(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    wished_items = models.ForeignKey(CartItem, on_delete=models.CASCADE, blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-added_date',]
        
        
    def __str__(self):
        return str(self.wished_items) 