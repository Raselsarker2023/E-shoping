from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.filters import SearchFilter

# Create your views here.

class OrderViewset(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name', 'email', 'address', 'product', 'status', 'phone', 'country']
    
    
class OrderListViewset(viewsets.ModelViewSet):
    queryset = models.OrderList.objects.all()
    serializer_class = serializers.OrderListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['product', 'order', 'quantity']