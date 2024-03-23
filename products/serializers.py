from rest_framework import serializers
from . import models

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        fields = '__all__'
        
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'