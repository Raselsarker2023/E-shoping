from rest_framework import serializers
from . import models

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'
        
        
class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderList
        fields = '__all__'