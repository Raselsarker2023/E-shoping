from rest_framework import serializers
from . import models
from products.serializers import ProductModelSerializer
from .models import CartItem, Cart
from products.models import ProductModel



class CartItemSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer(many=False)
    total_price = serializers.SerializerMethodField( method_name="total")
    
    class Meta:
        model = models.CartItem
        fields = '__all__'
        
    def total(self, CartItem:CartItem):
        return CartItem.quantity * CartItem.product.price
    
    
    

class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.UUIDField()
    
    def validate_product_id(self, value):
        if not ProductModel.objects.filter(pk=value).exists():
            raise serializers.ValidationError("There is no product associated with the given ID")
        
        return value
    
    def save(self, **kwargs):
        cart_id = self.context["cart_id"]
        product_id = self.validated_data["product_id"] 
        quantity = self.validated_data["quantity"] 
        
        try:
            cartitem = CartItem.objects.get(product_id=product_id, cart_id=cart_id)
            cartitem.quantity += quantity
            cartitem.save()
            
            self.instance = CartItem
            
        
        except:
            
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
            
        return self.instance
         

    class Meta:
        model = CartItem
        fields = ["id", "product_id", "quantity"]
    
    
    
class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')
    
    class Meta:
        model = models.Cart
        fields = '__all__'
        
        
    def main_total(self, cart: Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total
        
        

        
        
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wishlist
        fields = '__all__'