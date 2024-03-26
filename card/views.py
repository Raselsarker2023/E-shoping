from rest_framework import viewsets
from . import models, serializers
from rest_framework.filters import SearchFilter
from rest_framework import viewsets


# Create your views here.

class CartViewset(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer
    filter_backends = [SearchFilter]
    search_fields = ['total_price', 'username','product','quantity']
    
    

class CartItemViewset(viewsets.ModelViewSet):
    queryset = models.CartItem.objects.all()
    serializer_class = serializers.CartItemSerializer
    filter_backends = [SearchFilter]
    search_fields = ['product', 'quantity']
    
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.CartItemSerializer
        return serializers.CartItemSerializer
    

    
    
class WishlistAPIView(viewsets.ModelViewSet):
    queryset = models.Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer
    filter_backends = [SearchFilter]
    search_fields = ['wished_item']
