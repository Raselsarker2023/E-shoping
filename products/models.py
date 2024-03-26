from django.db import models
from django.contrib.auth.models import User
from categories.models import Category  
from .constants import STAR_CHOICES

# Create your models here.

class ProductModel(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True) 
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to='products/media/uploads', blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    


class Review(models.Model):
    product_name = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField()
    body = models.TextField(blank=True, null=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.name}"