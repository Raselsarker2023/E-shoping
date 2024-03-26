from rest_framework import serializers
from . import models


class CartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.CartItem
        fields = '__all__'        
        
        
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'
           

        
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wishlist
        fields = '__all__'
