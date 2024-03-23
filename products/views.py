from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from rest_framework import filters
from django.http import Http404


class ProductModelAPIView(viewsets.ModelViewSet):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category_name', 'description', 'rating']


    
from rest_framework.exceptions import ValidationError
import uuid

class ReviewAPIView(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email', 'body', 'rating']
    
    def create(self, request, *args, **kwargs):
        product_id = kwargs["pk"]
        if not self.is_valid_uuid(product_id):
            raise ValidationError({"product_id": ["Must be a valid UUID."]})
        request.data["reviewer"] = product_id
        return super().create(request, *args, **kwargs)
    
    def is_valid_uuid(self, uuid_to_test, version=4):
        try:
            uuid_obj = uuid.UUID(uuid_to_test, version=version)
        except ValueError:
            return False
        return str(uuid_obj) == uuid_to_test
    
    def get_queryset(self):
        return models.Review.objects.filter(reviewer_id=self.kwargs["pk"])




# class ReviewAPIView(viewsets.ModelViewSet):
#     queryset = models.Review.objects.all()
#     serializer_class = serializers.ReviewSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name', 'email', 'body', 'rating']
    
    
    # def create(self, request, *args, **kwargs):
    #     product_id = kwargs["product_id"]
    #     request.data["reviewer"] = product_id
    #     return super().create(request, *args, **kwargs)
    
    # def get_queryset(self):
    #      return models.Review.objects.filter(reviewer_id=self.kwargs["product_id"])

    

class ProductDetailAPIView(APIView):
    # queryset = models.ProductModel.objects.all()
    # serializer_class = serializers.ProductModelSerializer
    
    def get_object(self, pk):
        try:
            return models.ProductModel.objects.get(pk=pk)
        except models.ProductModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = serializers.ProductModelSerializer(product)
        return Response(serializer.data)
