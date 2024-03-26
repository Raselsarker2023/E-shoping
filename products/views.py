from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework import filters, pagination
from django.http import Http404
from rest_framework.pagination import PageNumberPagination



class ProductPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100
    
    
class ProductModelAPIView(viewsets.ModelViewSet):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category__name', 'description', 'rating']
    pagination_class = ProductPagination



class ReviewAPIView(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
   
    


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
