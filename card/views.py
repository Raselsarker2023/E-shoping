from rest_framework import viewsets
from . import models, serializers
from rest_framework.filters import SearchFilter
from .models import Cart, CartItem
from products.models import ProductModel
from . serializers import CartItemSerializer, AddCartItemSerializer
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework import viewsets, status
from rest_framework.response import Response


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
            return serializers.AddCartItemSerializer
        return serializers.CartItemSerializer
    



class AddCartItemViewSet(viewsets.ModelViewSet):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.AddCartItemSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(cart_id=request.data['cart_id'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
class WishlistAPIView(viewsets.ModelViewSet):
    queryset = models.Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['wished_item']





@permission_classes([permissions.IsAuthenticated])
class DeleteItemAPIView(viewsets.ModelViewSet):
    queryset = models.CartItem.objects.all()
    serializer_class = serializers.CartItemSerializer


@permission_classes([permissions.IsAuthenticated])
class AddItemAPIView(viewsets.ModelViewSet):
    queryset = models.CartItem.objects.all()
    serializer_class = serializers.AddCartItemSerializer

    def perform_create(self, serializer):
        serializer.save()